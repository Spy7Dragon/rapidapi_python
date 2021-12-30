from unittest import TestCase

from api.rapidapi_python.src.rapidapiclient import RapidApiClient
from utilities.api_key_io import get_rapidapi_key


class TestRapidApiSymbols(TestCase):
    def test_get_meta_data(self):
        symbol = 'AMZN'
        client = RapidApiClient(get_rapidapi_key())
        meta_data = client.symbols.get_meta_data(symbol)
        print(meta_data)

    def test_get_profile(self):
        symbols = ['AMZN']
        client = RapidApiClient(get_rapidapi_key())
        profile = client.symbols.get_profile(symbols)
        print(profile)

    def test_get_summary(self):
        symbols = ['AMZN']
        client = RapidApiClient(get_rapidapi_key())
        summary = client.symbols.get_summary(symbols)
        print(summary)
