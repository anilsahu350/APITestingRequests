import json
import pytest


@pytest.fixture(autouse=True)
def load_json_fixture(request):
    with open(r".\Day6\complex.json", "r") as file:
        request.cls.json_response = json.load(file)


class TestParseComplexJSONResponse:
    def test_user_details_validation(self):
        #verify status
        assert self.json_response["status"] == "success", " Wrong status code"

        #validate user details
        user_details = self.json_response["data"]["userDetails"]
        assert user_details['id'] == 12345, "wrong userid"
        assert user_details['name'] == "John Doe", "Wrong Name"
        assert user_details['email'] == "john.doe@example.com", "Wrong email"

        #Validate Home Phone Number
        home_phone = user_details["phoneNumbers"][0]
        assert home_phone["type"] == 'home', "wrong Type"
        assert home_phone['number'] == "123-456-7890", "wrong number"

        #validate Geo Coordinates
        geo = user_details["address"]["geo"]
        assert geo["latitude"] == 39.7817, "Wrong Latitude"
        assert geo["longitude"] == -89.6501, "Wrong Longitude"

        #Validate Preferences
        preferences = user_details["preferences"]
        assert preferences["notifications"] is True, "Expected notifications to be True"
        assert preferences["theme"] == "dark", "Wrong Theme"

    def test_recent_orders_validation(self):
        recent_orders = self.json_response["data"]["recentOrders"]

        #verify total number of orders
        assert len(recent_orders) == 2, "Expected only 2 orders"

        #Validate First order details
        first_order = recent_orders[0]
        assert first_order["orderId"] == 101, "Order Mismatch"
        assert first_order["totalAmount"] == 1226.49, "Total Amount Mismatch"
        items = recent_orders[0]["items"]
        assert items[1]["name"] == "Mouse", "Item name mismatch"

        # Validate second order details
        second_order = recent_orders[1]
        assert len(second_order['items']) == 1, "Items count mismatch"
        second_order_items = second_order['items'][0]
        assert second_order_items["name"] == "Smartphone", "Item name mismatch"
        assert second_order_items["price"] == 799.99, "Price mismatch"

    def test_preferences_and_metadata_validation(self):
        # Validate Preferences --> Languages
        preferences = self.json_response["data"]["userDetails"]["preferences"]
        languages = preferences["languages"]
        assert len(languages) == 3
        assert languages[0] == "English"
        assert languages[1] == "Spanish"
        assert languages[2] == "French"

        #Validate Metadata
        metadata = self.json_response["meta"]
        assert metadata["requestId"] == "abc123xyz"
        assert metadata["responseTimeMs"] == 250, "Response Time mismatch"