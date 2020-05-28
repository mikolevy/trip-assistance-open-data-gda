import dataclasses
import datetime
import json
import math
import os
from dataclasses import dataclass
from typing import List, Optional

import requests


@dataclass
class Vehicle:
    line_number: str
    latitude: float
    longitude: float

    @property
    def location(self):
        return self.latitude, self.longitude


VEHICLES_DATA_URL = "https://ckan2.multimediagdansk.pl/gpsPositions"


def load_vehicles_data() -> List[Vehicle]:
    vehicles_response = requests.get(VEHICLES_DATA_URL)
    vehicles_data = vehicles_response.json()

    return [
        Vehicle(line_number=vehicle_info["Line"], latitude=vehicle_info["Lat"], longitude=vehicle_info["Lon"],)
        for vehicle_info in vehicles_data["Vehicles"]
    ]


@dataclass
class BusStop:
    identifier: int
    name: str
    latitude: float
    longitude: float

    @property
    def location(self):
        return self.latitude, self.longitude


def load_all_bus_stops(date: str) -> List[BusStop]:
    path_to_data_file = os.path.join("bus_data", "bus_stops.json")
    with open(path_to_data_file) as bus_stops_file:
        bus_stops_by_date = json.load(bus_stops_file)

    bus_stops_data = bus_stops_by_date[date]["stops"]
    return [
        BusStop(
            identifier=bus_info["stopId"],
            name=bus_info["stopDesc"],
            latitude=bus_info["stopLat"],
            longitude=bus_info["stopLon"],
        )
        for bus_info in bus_stops_data
    ]


@dataclass
class BusStopOnRide(BusStop):
    order: int
    time: datetime.time


@dataclass
class BusRide:
    line_number: str
    stops: List[BusStopOnRide]

    def stop_by_id(self, stop_id: int) -> Optional[BusStopOnRide]:
        for stop in self.stops:
            if stop.identifier == stop_id:
                return stop


def load_bus_rides_for_line(selected_line_number: str, date: str) -> List[BusRide]:
    all_bus_stops = load_all_bus_stops(date)
    bus_stop_by_id = {bus_stop.identifier: bus_stop for bus_stop in all_bus_stops}
    file_name = f"{selected_line_number}.json"
    path_to_data_file = os.path.join("bus_data", "schedules", date, file_name)
    with open(path_to_data_file) as schedules_file:
        schedules_data = json.load(schedules_file)

    previous_stop_order = math.inf
    bus_rides = []
    for stop_info in schedules_data["stopTimes"]:

        stop_order = stop_info["stopSequence"]
        if stop_order < previous_stop_order:
            ride = BusRide(line_number=selected_line_number, stops=[])
            bus_rides.append(ride)

        stop_id = stop_info["stopId"]
        base_bus_date = bus_stop_by_id[stop_id]
        time = datetime.datetime.strptime(stop_info["departureTime"], "%Y-%m-%dT%H:%M:%S").time()
        bus_stop_on_ride = BusStopOnRide(**dataclasses.asdict(base_bus_date), order=stop_order, time=time,)
        ride.stops.append(bus_stop_on_ride)

        previous_stop_order = stop_order

    return bus_rides
