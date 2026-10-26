import requests


def test_pathParams():
    country = "Canada"
    response = requests.get(f"https://restcountries.com/v2/name/{country}")
    assert response.status_code == 200
    print(response.json())

def test_queryParams():
    query_parms = {"page": 2}
    HEADERS = {
        "Content-Type": "application/json",
        "x-api-key": "reqres-free-v1"
    }

    res = requests.get("https://reqres.in/api/users", params=query_parms, headers=HEADERS)
    print(res.status_code)
    print(res.json())