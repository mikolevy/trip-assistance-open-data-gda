from data_loaders import load_vehicles_data, load_all_bus_stops, load_bus_rides_for_line
from geo_location import address_to_location, bus_stops_in_range
from map import generate_map
from trip_recommender import recommend_trip
from user_interface import (
    ask_for_src_address,
    ask_for_line_number,
    ask_for_dst_address,
    print_info_about_trip,
    print_no_bus_info,
)

WALK_DISTANCE_IN_M = 400

DATE = "2020-05-27"


def run_trip_assistance():
    all_bus_stops = load_all_bus_stops(DATE)

    selected_line_number = ask_for_line_number()

    src_address = ask_for_src_address()
    src_point = address_to_location(src_address)
    src_bus_stops = bus_stops_in_range(src_point, WALK_DISTANCE_IN_M, all_bus_stops)

    dst_address = ask_for_dst_address()
    dst_point = address_to_location(dst_address)
    dst_bus_stops = bus_stops_in_range(dst_point, WALK_DISTANCE_IN_M, all_bus_stops)

    vehicles = load_vehicles_data()

    bus_rides = load_bus_rides_for_line(selected_line_number, DATE)
    trip = recommend_trip(src_bus_stops, dst_bus_stops, bus_rides)

    if trip:
        generate_map(vehicles, trip)
        print_info_about_trip(trip)
    else:
        print_no_bus_info()


if __name__ == "__main__":
    run_trip_assistance()
