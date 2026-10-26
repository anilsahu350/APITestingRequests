import requests
import json

class TestOrderAPI:
    BASE_URL = "https://simple-books-api.click/orders"
    AUTH_TOKEN = 'Bearer e6603d02aa73a06806ab22066bb2cc72eb21ecfff461dfd191cce8b9f0d86855'

    def test_submit_delete_order(self):
        # Submit Order
        payload = {
            "bookId": 1,
            "customerName": "John"
        }

        headers = {
            "Authorization": self.AUTH_TOKEN,
            "Content-Type": "application/json"
        }

        res = requests.post(self.BASE_URL, headers=headers, data=json.dumps(payload))

        assert res.status_code == 201, "wrong status code"
        order_id = res.json()["orderId"]
        print("Order Submitted with orderid = ", order_id)

        # Delete Order
        del_res = requests.delete(f"{self.BASE_URL}/{order_id}", headers=headers)
        assert del_res.status_code == 204, "Order not deleted"
        print("Order Deleted")