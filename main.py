# first line
from datetime import datetime

event_name = input("Enter the name of this event: ")

d = {}
d.update({"year": int(input("Enter the year: "))})
d.update({"month": int(input("Enter the month: "))})
d.update({"day": int(input("Enter the day: "))})

target_date = datetime(year=d["year"], month=d["month"], day=d["day"])
countdown = target_date - datetime.now()
print(f"Countdown to {event_name}: {countdown}")
