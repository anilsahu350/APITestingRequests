import pytest
import requests
import json

student_id = None   # Global variable
BASE_URL = "http://localhost:3000/students"
request_headers = {"Content-Type": "application/json"}


# Python Custom Class
def test_createStudentUsing_PythonCustomClass():
    global student_id

    class Student:
        def __init__(self, name, location, phone, courses):
            self.name = name
            self.location = location
            self.phone = phone
            self.courses = courses

    student = Student("Supriti", "Japan", "123456789",
                      ["Python", "Java"])
    request_body = student.__dict__

    # automatically dictionary converted to JSON
    response = requests.post(BASE_URL, json=request_body)

    # Manually dictionary converted to JSON
    # response = requests.post(BASE_URL, data=json.dumps(request_body), headers=request_headers)

    assert response.status_code == 201, "Status code is not 201"
    response_body = response.json()
    assert response_body["name"] == "Supriti", "Name is not correct"
    assert response_body["location"] == "Japan", "Location is not correct"
    assert response_body["phone"] == "123456789", "Phone is not correct"
    assert response_body["courses"][0] == "Python", "Course 1 should be Python"
    assert response_body["courses"][1] == "Java", "Course 2 should be Java"
    student_id = response_body["id"]
    print(response.json())

@pytest.fixture(autouse=True)
def delete_student():
    yield
    response = requests.delete(f"{BASE_URL}/{student_id}")
    assert response.status_code == 200, "Wrong Status code"
    print(response.json())
    print("Student Deleted")
