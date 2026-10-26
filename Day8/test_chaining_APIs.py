import pytest
import requests
import json
from faker import Faker

BASE_URL = "https://gorest.co.in/public/v2/users"
TOKEN = "362ea0e7a57ddc23e2cafb42a69386a3ee3271202c6d1538d2cb44dcb3c48eec"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}
faker = Faker()


class TestChainingAPIs:
    user_id = None   #class variable

    @pytest.mark.dependency(name="create")
    def test_create_user(self):
        data = {
            "name": faker.name(),
            "gender": "Male",
            "email": faker.unique.email(),
            "status": "inactive"
        }
        res = requests.post(BASE_URL, json=data, headers=HEADERS)
        assert res.status_code == 201, "wrong status code"
        TestChainingAPIs.user_id = res.json()["id"]
        assert TestChainingAPIs.user_id, "USER_ID is not generated"
        print("\nCREATE Response\n", json.dumps(res.json(), indent=4))

    @pytest.mark.dependency(depends=["create"])
    def test_get_user_details(self):
        res = requests.get(f"{BASE_URL}/{TestChainingAPIs.user_id}", headers=HEADERS)
        assert res.status_code == 200, "Get user failed"
        print("\nGET Response\n", json.dumps(res.json(), indent=4))

    @pytest.mark.dependency(depends=["create"])
    def test_update_user(self):
        updated_data = {
            "name": faker.name(),
            "gender": "Male",
            "email": faker.unique.email(),
            "status": "active"
        }
        res = requests.put(f"{BASE_URL}/{TestChainingAPIs.user_id}", json=updated_data, headers=HEADERS)
        assert res.status_code == 200, "wrong status code"
        print("\nUPDATE Response\n", json.dumps(res.json(), indent=4))

    @pytest.mark.dependency(depends=["create"])
    def test_delete_user(self):
        res = requests.delete(f"{BASE_URL}/{TestChainingAPIs.user_id}", headers=HEADERS)
        print("\nDelete Succesfully\n")
        assert res.status_code == 204, "wrong status code"