from typing import List

import folium

from data_loaders import Vehicle, BusStop, BusRide
from geo_location import StreetLocation
from trip_recommender import TripProposal

GDANSK_LOCATION = (54.3382, 18.60874)


def generate_map(
    vehicles: List[Vehicle], trip: TripProposal,
):
    trip_map = folium.Map(location=GDANSK_LOCATION, zoom_start=12)
    selected_line_number = trip.line_number
    src_bus_stop = trip.src_stop
    dst_bus_stop = trip.dst_stop

    for vehicle in vehicles:

        vehicle_info = f"Linia numer {vehicle.line_number}"
        if vehicle.line_number == selected_line_number:
            _create_circle_marker(vehicle.location, color="red", popup=vehicle_info).add_to(trip_map)

    stops_locations = [stop.location for stop in trip.stops_on_trip]
    folium.PolyLine(locations=stops_locations, color="red", weight=3, opacity=1).add_to(trip_map)

    for trip_stop in trip.stops_on_trip:
        _create_circle_marker(trip_stop.location, color="blue", popup=trip_stop.name).add_to(trip_map)

    _create_circle_marker(src_bus_stop.location, color="blue", popup=src_bus_stop.name).add_to(trip_map)
    _create_circle_marker(dst_bus_stop.location, color="green", popup=dst_bus_stop.name).add_to(trip_map)

    trip_map.save("trip_map.html")


def _create_circle_marker(location, color, popup) -> folium.CircleMarker:
    return folium.CircleMarker(
        location=location, popup=popup, color=color, fill_color=color, radius=7, fill=True, fill_opacity=1,
    )
