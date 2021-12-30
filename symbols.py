import requests

from api.rapidapi_python.rapid_api import RapidApi


class Symbols:
    url_extension = 'symbols/'

    def __init__(self, symbol):
        self.querystring = {"symbols": symbol}

    @staticmethod
    def build_url(method):
        url = RapidApi.base_url + Symbols.url_extension + method
        return url

    def get_meta_data(self):
        url_method = 'get-meta-data'
        url = Symbols.build_url(url_method)
        response = requests.request("GET", url, headers=RapidApi.headers, params=self.querystring)
        return response.json()

    def get_profile(self):
        url_method = 'get-profile'
        url = Symbols.build_url(url_method)
        response = requests.request("GET", url, headers=RapidApi.headers, params=self.querystring)
        return response.json()

    def get_summary(self):
        url_method = 'get-summary'
        url = Symbols.build_url(url_method)
        response = requests.request("GET", url, headers=RapidApi.headers, params=self.querystring)
        return response.json()
