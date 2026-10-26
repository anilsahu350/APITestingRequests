import requests


class TestHeaders:
    def test_headers_in_response(self):  # method name hidden by the popup menu
        url = "https://www.google.com/"
        res = requests.get(url)

        assert res.status_code == 200, "Wrong status code"

        #Captrure all headers
        all_headers = res.headers
        print("All Headers: ", all_headers)

        #Extract a specific header
        print("Date Header Value: ", all_headers["Date"])

        #Assertions
        assert res.status_code == 200, "Wrong status"
        assert "text/html" in res.headers.get("Content-Type", ""), "Wrong Content-Type"
        assert res.headers.get("Content-Encoding") is not None, "Missing Content-Encoding"
        assert res.headers.get("Content-Encoding") == "gzip", "Wrong Content-Encoding"
        assert res.headers.get("X-Frame-Options") == "SAMEORIGIN", "Wrong X-Frame-Options"
        assert res.headers.get("Server") == "gws", "Wrong Server"