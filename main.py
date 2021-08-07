# first line
from datetime import datetime

PYCON_DATE = datetime(year=2021, month=9, day=11, hour=0)
countdown = PYCON_DATE - datetime.now()
print(f"Countdown to my birthday: {countdown}")
