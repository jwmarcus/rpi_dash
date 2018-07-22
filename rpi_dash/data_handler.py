import json
import os

print(os.getcwd())

class Data_Handler():

    PATH = 'rpi_dash/static/data/forecast.json'
    weather_data = {}

    def __init__(self):
        # we only have one set of data right now
        self.weather_data = self._load_local_data(self.PATH)

    def refresh_data(self):
        # TODO: Implement
        # Refresh data in this class
        pass

    def get_data(self):
        # TODO: Implement, add type in here too.
        # Is loaded data recent? If not, get new data
        # Return the latest data for the page
        return self.weather_data

    def _load_local_data(self, path):
        payload = {}
        with open(path) as f:
            payload = json.load(f)
        return payload
