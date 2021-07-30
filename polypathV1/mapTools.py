import csv

def makeMapsURL(ID,CSVname): #Used to make the Maps URL for either a building or a Parking lot.
    
    csv_file = csv.reader(open(CSVname,"r"), delimiter=",")
    lat = ""
    log = ""
    found = False

    for row in csv_file:
        if CSVname == 'building.csv' or CSVname == 'parking.csv':
            ID = ID.upper()

        # if current rows 2nd value is equal to input, print that row
        if  ID == row[0]:
            lat = row[1]
            log = row[2]
            found = True

    if found:
        mapsURL = "https://maps.google.com/?saddr=Current+Location&daddr=" + lat + "%2C" + log + "&travelmode=walking"
    
    else:
        mapsURL = ""

    return mapsURL
