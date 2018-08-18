import json
import os
import time, datetime

import requests

class Data_Handler():

    DATA_PATHS = {}
    API_PATHS = {}

    weather_data = None

    def __init__(self):
        # set API and file paths:
        self.DATA_PATHS['weather'] = 'starnet/static/data/forecast.json'
        self.API_PATHS['weather'] = 'https://api.darksky.net/forecast/' + os.environ['WEATHER_API_KEY'] + '/42.37,-71.0828'

    def _refresh_external_weather_data(self):
        print("INFO {}: Firing off weather data request".format(datetime.datetime.now()))

        r = requests.get(
            self.API_PATHS['weather']
        )

        # Set initial weather data
        w_json = r.json()
        w_json['last_refresh_time'] = int(time.time())

        with open(self.DATA_PATHS['weather'], 'w') as f:
            json.dump(w_json, f)

        self.weather_data = w_json
        return w_json

    def get_data(self):
        w_json = None

        if os.path.isfile(self.DATA_PATHS['weather']):
            with open(self.DATA_PATHS['weather']) as f:
                w_json = json.load(f)

        # no file
        if w_json is None:
            w_json = self._refresh_external_weather_data()

        # no last_refresh_time set
        if 'last_refresh_time' not in w_json.keys():
            w_json = self._refresh_external_weather_data()

        # old data - this can dial down to 6 seconds and not cost at this point
        if (int(time.time()) - w_json['last_refresh_time']) > 120:
            w_json = self._refresh_external_weather_data()

        return w_json
