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
import csv  # Used to read CSV files
import sys  # Used for sys operations

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`
app = Flask(__name__)

@app.route('/requestMap')
def requestGetURL():
    buildID = request.args.get('buildID')
    isParking = request.args.get('parking')
    mapsURL = makeMapsURL(buildID,isParking)
    print(buildID, " ", isParking)
    return redirect(mapsURL, code=302)

@app.route('/<string:buildID>')
def directGetMapsURL(buildID):
    # Will generate link to BuildingID
    mapsURL = makeMapsURL(buildID,0)
    return redirect(mapsURL, code=302)

@app.route('/')
def root():
    return render_template('indexHome.html')


def makeMapsURL(buildID,isParking):
    
    if isParking == None:
        csv_file = csv.reader(open('building.csv', "r"), delimiter=",")
    else:
        csv_file = csv.reader(open('parking.csv',"r"), delimiter=",")


    for row in csv_file:
        # if current rows 2nd value is equal to input, print that row
        if buildID == row[0]:
            lat = row[1]
            log = row[2]

    mapsURL = "https://www.google.com/maps/search/?api=1&query=" + lat + "%2C" + log + "&travelmode=walking"
    return mapsURL


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
