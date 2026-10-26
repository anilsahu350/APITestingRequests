import requests, json

BASE_URL = "https://gorest.co.in/public/v2/users"
TOKEN = "362ea0e7a57ddc23e2cafb42a69386a3ee3271202c6d1538d2cb44dcb3c48eec"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}


class TestGetUser:
    def test_get_user(self, create_user):
        user_id = create_user
        assert user_id is not None, "User ID not set by create user test"
        response = requests.get(f"{BASE_URL}/{user_id}", headers=HEADERS)
        assert response.status_code == 200, "User fetch failed"
        print("\nGET Response:\n", json.dumps(response.json(), indent=4))