import pytest
import requests
import json

student_id = None   # Global variable
BASE_URL = "http://localhost:3000/students"
request_headers = {"Content-Type": "application/json"}


#External File
def test_createStudentUsingExternalFile():
    global student_id
    with open(r".\Day3\body.json", "r") as file:
        request_body = json.load(file)

    # automatically dictionary converted to JSON
    response = requests.post(BASE_URL, json=request_body)

    # Manually dictionary converted to JSON
    # response = requests.post(BASE_URL, data=json.dumps(request_body), headers=request_headers)

    assert response.status_code == 201, "Status code is not 201"
    response_body = response.json()
    assert response_body["name"] == "Scott", "Name is not correct"
    assert response_body["location"] == "France", "Location is not correct"
    assert response_body["phone"] == "123456", "Phone is not correct"
    assert response_body["courses"][0] == "C", "Course 1 should be C"
    assert response_body["courses"][1] == "C++", "Course 2 should be C++"
    student_id = response_body["id"]
    print(response.json())

@pytest.fixture(autouse=True)
def delete_student():
    yield
    response = requests.delete(f"{BASE_URL}/{student_id}")
    assert response.status_code == 200, "Wrong Status code"
    print(response.json())
    print("Student Deleted")
