import time
import datetime as dt
import csv  # Used to read CSV files

def makeEventList():

    currentTime = time.time()

    data = csv.reader(open('events.csv',"r"), delimiter=",")
    currentEvents = list()
    for row in data:
        showTime = time.mktime(time.strptime(row[3], "%d-%b-%y:%H:%M:%S"))
        endTime = time.mktime(time.strptime(row[5], "%d-%b-%y:%H:%M:%S"))
        if currentTime > showTime and currentTime < endTime:
            currentEvents.append(row)
    return currentEvents


