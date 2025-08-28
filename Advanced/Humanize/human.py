from datetime import datetime, timedelta

import humanize

print(humanize.intword(123456789))  # Output: '123 million
print(humanize.intcomma(123456789))
print(humanize.ordinal(23))  # Output: '23rd'
print(humanize.apnumber(0))  # works for 0-9
print(humanize.fractional(0.5))

file_size = 123456789
print(f"File size: {humanize.naturalsize(file_size)}")

# Using binary units
print(f"File size (binary): {humanize.naturalsize(file_size, binary=True)}")

# Using GNU-style prefixes
print(f"File size (GNU): {humanize.naturalsize(file_size, gnu=True)}")

# Custom format
print(f"File size (custom format): {humanize.naturalsize(file_size, format='%.2f')}")

past_date = datetime.now() - timedelta(days=2)
print(past_date, humanize.naturaltime(past_date))

some_date = datetime(2022, 7, 8)
print(humanize.naturaldate(some_date))

today = datetime.now()
tomorrow = today + timedelta(days=1)
print(humanize.naturalday(today))  # works only for yesterday, today and tomorrow
print(humanize.naturalday(tomorrow))  # works only for yesterday, today and tomorrow

duration = timedelta(days=2, hours=3, minutes=30)
print(humanize.precisedelta(duration))

# Using naturaldelta for time durations
delta1 = timedelta(days=3, hours=5)
print(f"Time duration: {humanize.naturaldelta(delta1)} from now")

# Example of a future duration (delta2)
delta2 = timedelta(hours=5)
print(f"Future duration: in {humanize.naturaldelta(delta2)}")

# Example of a past duration (delta3)
delta3 = timedelta(days=1, hours=3)
print(f"Past duration: {humanize.naturaldelta(delta3)} ago")
