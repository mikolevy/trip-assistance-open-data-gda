from dataclasses import dataclass
from typing import List

from geopy import Nominatim
from geopy.distance import distance

from data_loaders import BusStop


@dataclass
class StreetLocation:
    address: str
    latitude: float
    longitude: float

    @property
    def location(self):
        return self.latitude, self.longitude


def address_to_location(address: str) -> StreetLocation:
    geolocator = Nominatim(user_agent="webinar-agent")
    address_code = geolocator.geocode(address)
    return StreetLocation(address=address, latitude=address_code.latitude, longitude=address_code.longitude)


def bus_stops_in_range(reference_point: StreetLocation, distance_in_m: int, all_bus_stops: List[BusStop]):
    return [
        bus_stop
        for bus_stop in all_bus_stops
        if distance(reference_point.location, bus_stop.location).meters <= distance_in_m
    ]
