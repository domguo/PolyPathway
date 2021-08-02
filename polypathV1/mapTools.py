import csv
import requests

def makeMapsURL(ID,CSVname): #Used to make the Maps URL for either a building or a Parking lot.
    
    csv_file = csv.reader(open(CSVname,"r"), delimiter=",")
    lat = ""
    log = ""
    found = False

    if CSVname == 'building.csv' or CSVname == 'parking.csv':
        ID = ID.upper()

    for row in csv_file:
        if CSVname == 'building.csv' or CSVname == 'parking.csv':
            ID = ID.upper()

        # if current rows 2nd value is equal to input, print that row
        if  ID == row[0]:
            lat = row[1]
            log = row[2]
            found = True
            break

    if found:
        mapsURL = "https://maps.google.com/?daddr=" + lat + "%2C" + log + "&travelmode=walking&dir_action=navigate"
    
    else:
        mapsURL = ""

    return mapsURL

def getCoords(ID,CSVname): #Used to make the Maps URL for either a building or a Parking lot.
    
    csv_file = csv.reader(open(CSVname,"r"), delimiter=",")
    lat = ""
    log = ""
    found = False

    ID = ID.upper()

    for row in csv_file:
        if CSVname == 'building.csv' or CSVname == 'parking.csv':
            ID = ID.upper()

        # if current rows 2nd value is equal to input, print that row
        if  ID == row[0]:
            lat = row[1]
            log = row[2]
            found = True
            break

    if found:
        dict = {"lat": lat, "long": log}
    
    else:
        dict = {}

    return dict


def getDistance(ID1, ID2, park1, park2, coords1, coords2):

    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

    params = dict(
        origin='',
        destination='',
        mode='walking',
        language='en-EN',
        key='AIzaSyCnQLfehLWCsHMsay61rzCnF4JelH4VqVU'

    )

    print(coords1)
    print(coords2)

    #resp = requests.get(url = url, params = params)
    #data = resp.json()
