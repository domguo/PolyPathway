import csv
import urllib.request as requests
import json

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

def getCoords(ID,CSVname): #Used to get coordinates of a building, returns a dictionary
    
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

    url = 'https://maps.googleapis.com/maps/api/distancematrix/json'

    url += '?origins=' + coords1['lat'] + '%2C' + coords1['long']
    url += '&destinations=' + coords2['lat'] + '%2C' + coords2['long']
    url += '&units=imperial'
    url += '&mode=walking'
    url += '&key=AIzaSyB8bGbnUsSdSd-pqSBuAixTFWNH6V80PPc'

    resp = requests.urlopen(url)

    data = json.load(resp)

    distance = data['rows'][0]['elements'][0]['distance']['text']
    duration = data['rows'][0]['elements'][0]['duration']['text']

    output = 'The distance from '

    if park1:
        output += 'parking lot ' + ID1 + ' '
    else:
        output += 'building ' + ID1 + ' '

    output += 'to '

    if park2:
        output += 'parking lot ' + ID2 + ' '
    else:
        output += 'building ' + ID2 + ' '

    output += 'is: \n'
    output += distance + '\n'
    output += duration + '\n'

    return output

#   Google Maps Distance Matrix URL format
#   https://maps.googleapis.com/maps/api/distancematrix/outputFormat?parameters

#   https://maps.googleapis.com/maps/api/distancematrix/json?
#   origins=Vancouver+BC        For coordinates, 'latitude' + %2C + 'longitude'
#   &destinations=San+Francisco
#   &units=imperial
#   &mode=walking
#   &language=en-EN
#   &key=AIzaSyCnQLfehLWCsHMsay61rzCnF4JelH4VqVU

#   API Key: AIzaSyCnQLfehLWCsHMsay61rzCnF4JelH4VqVU  ONLY VALID FOR TESTING

#   Time is in seconds