import requests
import pytest

user_id = None

HEADERS = {
    "Content-Type": "application/json",
    "api-key": "postmanrulz"
}


@pytest.mark.order(1)
def test_get_users_001():
    res = requests.get("https://library-api.postmanlabs.com/books", headers=HEADERS)
    assert res.status_code == 200, "Wrong status"
    assert res.headers["Content-Type"] == "application/json; charset=utf-8", "Wrong content type"
    assert res.elapsed.total_seconds() < 10, "Too slow"
    data = res.json()
    assert isinstance(data, list), "Response is not a list"
    assert len(data) > 0, "No books found"
    # print(data)
    assert "id" in data[0], "ID missing"
    assert "title" in data[0], "Title missing"
    assert "author" in data[0], "Author missing"

    # assert data.get("data") is not None, "Data missing"
    # print(data)
    # assert data.get("page") == 2, "Wrong page"
    # assert "email" in res.text, "Email not found"


@pytest.mark.dependency()
@pytest.mark.order(2)
def test_create_user_001():
    global user_id
    payload = {"title": "Learn postman with Anil-01","author": "Anil","genre": "Computer Science","yearPublished": 2026}
    res = requests.post("https://library-api.postmanlabs.com/books", json=payload, headers=HEADERS)
    assert res.status_code == 201, "Wrong status"
    assert res.headers["Content-Type"] == "application/json; charset=utf-8", "Wrong content type"
    assert res.elapsed.total_seconds() < 10, "Too slow"
    data = res.json()
    assert data.get("author") == "Anil", "Author mismatch"
    assert data.get("genre") == "Computer Science", "Genre mismatch"
    assert "id" in data, "ID missing"
    user_id = data["id"]
    print("user_id:", user_id)
    print(data)

    # assert "id" in data[0], "ID missing"
    # assert "title" in data[0], "Title missing"
    # assert "author" in data[0], "Author missing"


@pytest.mark.order(3)
@pytest.mark.dependency(depends=["test_create_user_001"])
def test_update_user_001():
    payload = {"title": "Learn postman with Anil-Updated","author": "kumar","genre": "teacher","yearPublished": 2026}
    res = requests.patch(f"https://library-api.postmanlabs.com/books/{user_id}", json=payload, headers=HEADERS)
    assert res.status_code == 200, "Wrong status"
    assert res.headers["Content-Type"] == "application/json; charset=utf-8", "Wrong content type"
    assert res.elapsed.total_seconds() < 10, "Too slow"
    data = res.json()
    assert data.get("author") == "kumar", "Author mismatch"
    assert data.get("genre") == "teacher", "Genre mismatch"
    assert data.get("genre") == "teacher", "Genre mismatch"
    assert data.get("yearPublished") == 2026, "Year mismatch"
    print(data)


@pytest.mark.order(4)
@pytest.mark.dependency(depends=["test_create_user_001"])
def test_delete_user_001():
    res = requests.delete(f"https://library-api.postmanlabs.com/books/{user_id}", headers=HEADERS)
    assert res.elapsed.total_seconds() < 5, "Too slow"
    assert res.status_code == 204, "Wrong status"
    assert res.text == "", "Response not empty"
    print(f"** User ID:{user_id} deleted successfully...")