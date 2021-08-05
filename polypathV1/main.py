# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License. 

# [START gae_python38_app]
# [START gae_python3_app]

from flask import Flask, render_template, redirect, request  # Used to render and redirect
from mapTools import getCoords, getDistance, makeMapsURL
import timeTools
import csv  # Used to read CSV files
import sys  # Used for sys operations


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`
app = Flask(__name__)

@app.route('/userRequestMap')
def userRequestGetURL():
    buildID = request.args.get('buildID')
    isParking = request.args.get('parking')

    if isParking == None:
        csvfile = 'building.csv'
    else:
        csvfile = 'parking.csv'

    mapsURL = makeMapsURL(buildID, csvfile)
    print(buildID, " ", isParking, csvfile)

    if not mapsURL:
        return redirect('indexError', code=302)
    else:
        return redirect(mapsURL, code=302)

@app.route('/findDistance')
def calculateDistance():
    buildID1 = request.args.get('buildID1')
    buildID2 = request.args.get('buildID2')
    isParking1 = request.args.get('parking1')
    isParking2 = request.args.get('parking2')

    if isParking1 == None:
        csvfile1 = 'building.csv'
    else:
        csvfile1 = 'parking.csv'

    if isParking2 == None:
        csvfile2 = 'building.csv'
    else:
        csvfile2 = 'parking.csv'

    coords1 = getCoords(buildID1, csvfile1)
    coords2 = getCoords(buildID2, csvfile2)

    if len(coords1) == 0 or len(coords2) == 0:
        return redirect('distanceError', code=302)

    else:
        output = getDistance(buildID1, buildID2, isParking1, isParking2, coords1, coords2)

    return render_template('distance.html', variable = output)

@app.route('/LocationRequestMap')
def locationRequestGetURL():
    csvfile = 'KeyLocations.csv'
    buildID = request.args.get('locName')
    mapsURL = makeMapsURL(buildID, csvfile)
    return redirect(mapsURL, code=302)

@app.route('/events')
def directEvents():
    eventlistdata = timeTools.makeEventList()
    return render_template('events.html', eventlist=eventlistdata)

@app.route('/eventsGO')
def directeventLocation():
    eventID = request.args.get("eventID")
    mapsURL = makeMapsURL(eventID, 'events.csv')
    return redirect(mapsURL, code = 302)


@app.route('/<string:buildID>')
def directGetMapsURL(buildID):
    mapsURL = makeMapsURL(buildID,'building.csv') # Will generate link to BuildingID
    return redirect(mapsURL, code=302)

@app.route('/indexError')
def directErrorPage():
    return render_template('indexError.html')

@app.route('/locationHome')
@app.route('/locationhome')
def directLocationpage():
    return render_template('locationHome.html')

@app.route('/aboutus')
def directAboutUs():
    return render_template('aboutus.html')

@app.route('/contact')
def directContact():
    return render_template('contact.html')

@app.route('/campusMap')
def directCampusMap():
    return render_template('campusMap.html')

@app.route('/distance')
def directDistance():
    return render_template('distance.html')

@app.route('/distanceError')
def directDistanceError():
    return render_template('distanceError.html')

@app.route('/')
def root():
    return render_template('indexHome.html')

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]