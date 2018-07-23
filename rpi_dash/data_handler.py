import json, os

import requests

class Data_Handler():

    DATA_PATHS = {}
    API_PATHS = {}

    weather_data = None

    def __init__(self):
        # set API and file paths:
        self.DATA_PATHS['weather'] = 'rpi_dash/static/data/forecast.json'
        self.API_PATHS['weather'] = 'https://api.darksky.net/forecast/' + os.environ['WEATHER_API_KEY'] + '/42.37,-71.0828'

        r = requests.get(
            self.API_PATHS['weather']
        )

        # Set initial weather data
        self.weather_data = r.json()

    def get_data(self):
        return self.weather_data

    # def load_local_data(self, path):
    #     payload = {}
    #     with open(path) as f:
    #         payload = json.load(f)
    #     return payload
