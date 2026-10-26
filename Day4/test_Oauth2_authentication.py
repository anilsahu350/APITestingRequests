import pytest
import requests

access_token= None          #global variable

@pytest.fixture(scope="session", autouse=True)
def generate_token():
    global access_token
    client_id = "8d20043bc76d420987e4959b3b1f55d3"
    client_secret = "4ee22d9c8ca844a8a6373bf584b1956f"
    token_url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    form_data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    res = requests.post(token_url, data=form_data, headers=headers)
    assert res.status_code == 200, "Wrong Status Code"
    print(res.json())
    access_token = res.json()["access_token"]


    res = requests.post(token_url, data=form_data, headers=headers)
    assert res.status_code == 200, "Wrong Status Code"
    print(res.json())
    access_token = res.json()['access_token']
    print("access token:",access_token)


class TestOAuth2SpotifyAPI:
    def test_get_arjith_singh_top_tracks(self):
        assert access_token, "Token not generated"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        res = requests.get("https://api.spotify.com/v1/artists/4YRxDV8wJFPHPTeXepOstw/top-tracks", headers=headers, params={"market":"IN"})
        print(res.status_code, res.text)
        # assert res.status_code == 200, "Wrong Status Code"
        # print(res.json())
        tracks = res.json().get(["tracks"],[])
        print(tracks)
        for i,track in enumerate(tracks, start=1):
            print(f"{i}. {track['name']}")