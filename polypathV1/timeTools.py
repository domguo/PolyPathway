import time
import datetime # To get UTC time with tz info
import calendar # For calendar.timegm() function
import pytz # Timezone stuff
import csv  # Used to read CSV files

# Check if current time and given timezone is in DST
def is_dst(dt=None, timezone="UTC"):
    if dt is None:
        dt = datetime.datetime.utcnow()
    timezone = pytz.timezone(timezone)
    timezone_aware_date = timezone.localize(dt, is_dst=None)
    return timezone_aware_date.tzinfo._dst.seconds != 0

def makeEventList():
    currentTime = time.time()

    data = csv.reader(open('events.csv',"r"), delimiter=",")
    currentEvents = list()

    for row in data:
        # Pull dates and times from CSV, convert them to epoch time using calendar.timegm()
        showTime = calendar.timegm(time.strptime(row[3], "%d-%b-%y:%H:%M:%S"))
        endTime = calendar.timegm(time.strptime(row[5], "%d-%b-%y:%H:%M:%S"))

        # Convert from PST to UTC (60 seconds * 60 minutes * 8 hours)
        showTime += 28800
        endTime += 28800

        # Check if Daylight Savings time is active.
        # If DST is active, offset time by one hour (60 seconds * 60 minutes * 1 hour)
        if is_dst(timezone="US/Pacific"):
            showTime -= 3600
            endTime -= 3600

        if currentTime > showTime and currentTime < endTime:
            currentEvents.append(row)

    return currentEvents


