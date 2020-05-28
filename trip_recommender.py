import datetime
from dataclasses import dataclass
from typing import List, Optional

from data_loaders import BusStop, BusRide, BusStopOnRide


@dataclass
class TripProposal:
    line_number: str
    stops_on_trip: List[BusStopOnRide]

    @property
    def src_stop(self) -> BusStopOnRide:
        return self.stops_on_trip[0]

    @property
    def dst_stop(self) -> BusStopOnRide:
        return self.stops_on_trip[-1]

    @property
    def departure(self) -> datetime.time:
        return self.src_stop.time

    @property
    def arrival(self) -> datetime.time:
        return self.dst_stop.time


def recommend_trip(
    src_stops: List[BusStop], dst_stops: List[BusStop], bus_rides: List[BusRide]
) -> Optional[TripProposal]:
    for ride in bus_rides:

        for src_stop in src_stops:
            src_stop_on_ride = ride.stop_by_id(src_stop.identifier)

            if not src_stop_on_ride:
                continue

            for dst_stop in dst_stops:
                dst_stop_on_ride = ride.stop_by_id(dst_stop.identifier)

                if not dst_stop_on_ride:
                    continue

                if src_stop_on_ride.order > dst_stop_on_ride.order:
                    continue

                stops_start_index = ride.stops.index(src_stop_on_ride)
                stops_end_index = ride.stops.index(dst_stop_on_ride) + 1
                stops_on_trip = ride.stops[stops_start_index:stops_end_index]

                trip_proposal = TripProposal(line_number=ride.line_number, stops_on_trip=stops_on_trip)

                if trip_proposal.departure > datetime.datetime.now().time():
                    return trip_proposal
