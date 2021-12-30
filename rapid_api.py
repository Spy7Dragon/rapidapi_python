from utilities.api_key_io import get_rapidapi_key


class RapidApi:
    base_url = "https://seeking-alpha.p.rapidapi.com/"

    headers = {
            'x-rapidapi-host': "seeking-alpha.p.rapidapi.com",
            'x-rapidapi-key': get_rapidapi_key()
        }


