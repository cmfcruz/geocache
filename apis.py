import requests
from config import Config


class Google:

    def __init__(self):
        config = Config()
        self.url = config.apiurl

    def get_result(self, latitude, longitude, apikey):
        response = requests.get(self.url.format(latitude, longitude, apikey))
        result = response.json()
        return result
