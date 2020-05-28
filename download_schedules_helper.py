import json
import os

import requests

SCHEDULES_DIRECTORY = "schedules"


def load_schedule():
    date_indicator = "stopTimes?date="
    date_len = 10
    with open("stoptimes.json") as schedule_urls_file:
        schedule_urls = json.load(schedule_urls_file)
        total_buses_number = len(schedule_urls)
        for index, (bus_id, urls) in enumerate(schedule_urls.items()):
            print(f"{index * 100 / total_buses_number:.0f}%")
            for url in urls:
                date_start_index = url.index(date_indicator) + len(date_indicator)
                date = url[date_start_index : date_start_index + date_len]
                _create_directory_for_date(date)
                schedule_destination_path = os.path.join("schedules", date, f"{bus_id}.json")
                response = requests.get(url, allow_redirects=True)
                with open(schedule_destination_path, mode="wb") as schedule_destination_file:
                    schedule_destination_file.write(response.content)


def _create_directory_for_date(date: str) -> None:
    try:
        os.mkdir(os.path.join(SCHEDULES_DIRECTORY, date))
    except FileExistsError:
        pass


if __name__ == "__main__":
    load_schedule()
