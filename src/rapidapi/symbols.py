import requests


class Symbols:
    url_extension = 'symbols/'

    def __init__(self, client):
        self.client = client

    def get_meta_data(self, symbol):
        url_method = 'get-meta-data'
        url = self.client.build_url(Symbols.url_extension, url_method)
        query_string = {'symbol': symbol}
        response = requests.request("GET", url, headers=self.client.headers, params=query_string)
        return response.json()

    def get_profile(self, symbols):
        url_method = 'get-profile'
        url = self.client.build_url(Symbols.url_extension, url_method)
        query_string = {"symbols": ",".join(symbols)}
        response = requests.request("GET", url, headers=self.client.headers, params=query_string)
        return response.json()

    def get_summary(self, symbols):
        url_method = 'get-summary'
        url = self.client.build_url(Symbols.url_extension, url_method)
        query_string = {"symbols": ",".join(symbols)}
        response = requests.request("GET", url, headers=self.client.headers, params=query_string)
        return response.json()
