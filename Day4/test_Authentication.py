import os

import requests
from dotenv import load_dotenv

from requests.auth import HTTPDigestAuth

load_dotenv()
class TestAuthentication:
    def test_basic_auth(self):
        res = requests.get("https://postman-echo.com/basic-auth", auth=('postman', 'password'))
        assert res.status_code == 200, "Wrong Status Code"
        data = res.json()
        print(data)
        assert data.get("authenticated") is True

    def test_digest_auth(self):
        res = requests.get("https://postman-echo.com/digest-auth", auth=HTTPDigestAuth('postman', 'password'))
        assert res.status_code == 200, "Wrong Status Code"
        data = res.json()
        print(data)
        assert data.get("authenticated") is True

    def test_Bearer_token_auth(self):
        bearer_token = os.getenv("GITHUB_TOKEN") # token generated from github
        request_headers = {"Authorization": f"Bearer {bearer_token}"}
        res = requests.get("https://api.github.com/user/repos", headers=request_headers)
        assert res.status_code == 200, "Wrong Status Code"
        print(res.json())

    def test_api_key_auth(self):
        params = {
            "q": "Chennai",
            "appid": "85942c135789cdf1d1adb0111716cce5"  # API Key generated from weather
        }
        res = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
        assert res.status_code == 200, "Wrong Status Code"
        print(res.json())