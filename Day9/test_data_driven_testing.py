import pytest
import requests
import json

from Day9.test_data_providers import read_json_data, read_csv_data, read_excel_data

BASE_URL = "https://simple-books-api.click/orders"
AUTH_TOKEN = 'Bearer e6603d02aa73a06806ab22066bb2cc72eb21ecfff461dfd191cce8b9f0d86855'

def submit_delete_order(book_id,customer_name):

    #submit order
    payload = {
        "bookId": int(book_id),
        "customerName": customer_name
    }

    headers = {
        "Authorization": AUTH_TOKEN,
        "Content-Type": "application/json"
    }

    res = requests.post(BASE_URL,headers=headers,data=json.dumps(payload))

    assert res.status_code == 201, "wrong status code"
    order_id = res.json()["orderId"]
    print("Order Submitted with orderid = ", order_id)

    #Delete Order
    del_res = requests.delete(f"{BASE_URL}/{order_id}", headers=headers)
    assert del_res.status_code == 204,"Order not deleted"
    print("Order Deleted")

@pytest.mark.parametrize('order_data',read_json_data(r".\Day9\test_data\orders_json_data.json"))
def test_with_json_data(order_data):
    order_data = order_data[0]
    submit_delete_order(order_data["BookID"], order_data["CustomerName"])

# @pytest.mark.parametrize('order_data',read_json_data(r".\Day9\test_data\orders_json_data.json"))
# def test_with_json_data(order_data):
#     print("BEFORE:", order_data)
#     order_data = order_data[0]
#     print("AFTER:", order_data)

@pytest.mark.parametrize('book_id,customer_name',read_csv_data(r".\Day9\test_data\orders_csv_data.csv"))
def test_with_csv_data(book_id,customer_name):
    submit_delete_order(book_id, customer_name)

# Excel Test
@pytest.mark.parametrize("book_id, customer_name",
read_excel_data(r".\Day9\test_data\orders_excel_data.xlsx", "Sheet1"))
def test_with_excel_data(book_id, customer_name):
    submit_delete_order(book_id, customer_name)

