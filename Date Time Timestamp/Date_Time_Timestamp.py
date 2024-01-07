"""##############################################################################
Using Times, Dates & Timestamps in Python

Summary of Time and Date classes:
datetime # superclass for most of the date and time libraries
    date # general purpose date library
    time # general purpose time library
    datetime # for date and time in one object
    timedelta # for a duration or elapsed time
time # for Unix timestamp and process_time
calendar # for calendars
dateutil # extended datetime functionality, esp string parsing and delta calculation
##############################################################################"""

# Today's Date
# ---------------------------
# Use datetime.date.today()
# datetime.date class has the following integer attributes, date(year, month, day)
# get day of the week using date.weekday() # Monday is 0

from datetime import date
todays_date = date.today()
print(todays_date)
print(todays_date.month, todays_date.day, todays_date.year)
print(todays_date.weekday())

# ISO format is a string format, yyyy-mm-dd
# ---------------------------
# date_object.isoformat() does the same thing as str(date_object)

from datetime import date
todays_date = date.fromisoformat('2011-11-23')
print(todays_date)
print(str(todays_date))
print(todays_date.isoformat())
todays_date

# Comparison, addition and sutraction of dates
# ---------------------------
# Comparison gives boolean result. Later date is greater than earlier date.
# Date addition & subtraction give result as a datetime.timedelta object (explained more below).
# The same comparison and add/subtract operations can be used with time objects.

from datetime import date
todays_date = date.today()
d2 = date(2015, 5, 14)
print(todays_date > d2)
print(todays_date - d2)

# Time
# ---------------------------
# time objects have the following attributes, time(hour, minute, second, microsecond, tzinfo)
# use datetime.time to compare time objects: t1 < t2 if t1 occurs before t2
# attributes are all optional, so you can just work with hours and minutes if you want
# daylight savings is handled by the time.dst() function (if tzinfo is set)

from datetime import time
t1 = time(14, 25, 36, 18625)
print(t1)

t2 = time(2, 19)
print(t2)
print(t1 < t2)

# datetime.datetime combines date and time attributes into a datetime object
# ---------------------------
# datetime.datetime(year, month, day, hour, minute, second, microsecond, tzinfo)
# datetime.datetime objects can be used as dictionary keys
# includes functions: date(), time()

from datetime import datetime
dt1 = datetime(1941, 12, 7, 7, 53)
print(dt1)
print(dt1.date())
print(dt1.time())

# Use datetime.datetime.now() to get the current date and time

t3 = datetime.now()

print(t3.time())
print(t3.date())
print(t3.hour, t3.minute)
print(str(t3.month) + '-' + str(t3.day) + '-' + str(t3.year))

# Use datetime.strftime() to get names of months and weekdays.

t3 = datetime.now()
print(t3.strftime('%A'))
print(t3.strftime('%a, %A, %b, %B, %x'))

# A timedelta is used for a duration, or the time difference between two dates or times
# ---------------------------
# datetime.timedelta(days, seconds, microseconds)
# A timedelta can also be multiplied or divided by an integer or float

from datetime import timedelta, date, time
todays_date = date(2011, 6, 15)
d2 = date(2012, 9, 18)
td = d2 - todays_date
print(td, type(td))
print(td.total_seconds())
print(td * 3)

from datetime import datetime
today = datetime.today().date()
my_event = date(2021, 11, 6)
days_to_event = abs(my_event - today)
print(days_to_event.days, 'days to event.')
print(days_to_event, 'days to event.')

# Get a UNIX timestamp (time since the epoch)
# ---------------------------
# A timestamp is the time since Jan 1, 1970 in seconds
# Use time.time() to get timestamp
# Use datetime.fromtimestamp(ts) and datetime.timestamp(datetime_obj) to convert between timestamp and datetime
# Use time.process_time() to get runtime of an operation on your computer

import time
ts = time.time()
print(ts)
print(time.ctime(ts))


from datetime import datetime
now = datetime.fromtimestamp(ts)
print(now)
print(datetime.timestamp(now))

start_time = time.process_time()
# do some stuff
end_time = time.process_time()
print('operation executed in ', end_time - start_time)
