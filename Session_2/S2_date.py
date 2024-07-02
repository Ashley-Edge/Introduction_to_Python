from datetime import datetime

time_now = datetime.now()
print(time_now.strftime("It's %H:%M%p, on %A the %d of %B %Y."))

# output example "It's 19:42PM, on Tuesday the 02 of July 2024."

# Character codes examples:
# %a: Returns the first three characters of the weekday, e.g. Wed.
# %A: Returns the full name of the weekday, e.g. Wednesday.
# %B: Returns the full name of the month, e.g. September.
# %w: Returns the weekday as a number, from 0 to 6, with Sunday being 0.
# %m: Returns the month as a number, from 01 to 12.
# %p: Returns AM/PM for time.
# %f: Returns microsecond from 000000 to 999999.
# %Z: Returns the timezone.
# %Y: Returns the year in four digit format
# %b: Returns the first three characters of the month name.
# %d: Returns day of the month, from 1 to 31.
# %Y: Returns the year in four-digit format.
# %H: Returns the hour.
# %M: Returns the minute, from 00 to 59.
# %S: Returns the second, from 00 to 59.
