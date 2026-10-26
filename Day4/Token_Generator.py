import requests

access_token= None          #global variable

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
    print("access token is:", res.json()["access_token"])



generate_token()