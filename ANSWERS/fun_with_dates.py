from datetime import date as Date
import calendar

test_dates = (
    (1956, 10, 31),
    (1952, 9, 22),
    (1990, 8, 27),
)

for year, month, day in test_dates:
    dt = Date(year, month, day)
    wday = calendar.weekday(year, month, day)
    wday_name = calendar.day_name[wday]
    is_leapyear = calendar.isleap(year)
    print(f'{dt} {wday_name:10s} {is_leapyear}')
