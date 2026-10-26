import requests


class TestCookies:
    def test_cookies_in_resposne(self):
        url = "https://www.google.com/"
        res = requests.get(url)
        assert res.status_code == 200, "Wrong status code"
        #Capture all cookies
        all_cookies = res.cookies
        print("All cookies : ", all_cookies)

        # Assert Cookie and check if it is not none
        assert "AEC" in all_cookies, "AEC not found"
        assert all_cookies.get("AEC") is not None, "AEC is None"

        #Extract a specific Cookie
        cookie_value = all_cookies.get("AEC")
        print("Cookie value : ", cookie_value)

        #Iterate through each and every cookie and print
        for key, value in all_cookies.items():
            print(f"{key}: {value}")