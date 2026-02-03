print("SCRIPT STARTED")

import time
from scraper import fetch_events
from storage import upsert_events


def run(city):
    print(f"\nFetching events for {city}...")

    events = fetch_events(city)

    print(f"{len(events)} events found")

    upsert_events(events)

    print("Excel updated!")


def main():
    # USER SE CITY INPUT
    city = input("Enter city name: ").strip()

    if not city:
        print("❌ City name is required")
        return

    # run forever every 2 minutes
    while True:
        run(city)

        print("Waiting 2 minutes...\n")
        time.sleep(120)   # 120 seconds = 2 minutes


if __name__ == "__main__":
    main()

