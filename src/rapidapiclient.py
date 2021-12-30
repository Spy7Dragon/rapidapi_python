from api.rapidapi_python.src.rapidapi.symbols import Symbols


class RapidApiClient:
    base_url = "https://seeking-alpha.p.rapidapi.com/"

    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            'x-rapidapi-host': "seeking-alpha.p.rapidapi.com",
            'x-rapidapi-key': self.api_key
        }
        self.symbols = Symbols(self)

    def build_url(self, extension, method):
        url = RapidApiClient.base_url + extension + method
        return url


