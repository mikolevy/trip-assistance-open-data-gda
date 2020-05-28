from trip_recommender import TripProposal


def ask_for_src_address():
    return input("Skąd ruszasz? ")


def ask_for_line_number():
    return input("Jaką linią chcesz jechać? ")


def ask_for_dst_address():
    return input("Dokąd zmierzasz? ")


def print_info_about_trip(trip: TripProposal):
    src_stop = trip.src_stop.name
    dst_stop = trip.dst_stop.name
    line_number = trip.line_number
    departure = trip.departure
    arrival = trip.arrival
    print(f"Rusz o {departure} z przystanku {src_stop}")
    print(f"Jedz numerem {line_number} do przystanku {dst_stop}")
    print(f"Na miejscu będziesz {1 + 4} {arrival}")


def print_no_bus_info():
    print("Nie znaleziono połączenia")
