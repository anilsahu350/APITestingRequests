import json
import requests
import xmltodict
from xml.dom.minidom import parseString


class TestXMLParsing:
    # Basic XML element Validation
    def test_xml_response_1(self):
        """
        validates:
        - HTTP STATUS CODE
        - CONTENT TYPE
        - SPECIFIC XML ELEMENT VALUES
        """
        url = "https://mocktarget.apigee.net/xml"
        res = requests.get(url)

        assert res.status_code == 200, "Wrong status code"
        assert res.headers["Content-Type"] == "application/xml; charset=utf-8", "Wrong header"

        # pretty print of xml
        print(parseString(res.text).toprettyxml())

        # conversion of xml to json
        xml_data = xmltodict.parse(res.text)

        # pretty print of json
        print(json.dumps(xml_data, indent=4))

        # Specific element validations
        root = xml_data["root"]
        assert root["city"] == "San Jose"
        assert root["firstName"] == "John"
        assert root["lastName"] == "Doe"
        assert root["state"] == "CA"

    # Basic XML Attribute Validation
    def test_xml_response_2(self):
        """
        validates:
        - HTTP STATUS CODE
        - CONTENT TYPE
        - XML Attribute using @ notation
        """
        url = "https://httpbin.org/xml"
        res = requests.get(url)

        assert res.status_code == 200
        assert res.headers["Content-Type"] == "application/xml", "Wrong header"

        # pretty print of xml
        print(parseString(res.text).toprettyxml())

        # conversion of xml to json
        xml_data = xmltodict.parse(res.text)

        # pretty print of json
        print(json.dumps(xml_data, indent=4))

        # Extract and Validate attributes
        slideshow = xml_data["slideshow"]
        assert slideshow["@title"] == "Sample Slide Show"
        assert slideshow["@date"] == "Date of publication"
        assert slideshow["@author"] == "Yours Truly"

    # Parse and validate slide content
    def test_parsing_xml_response(self):
        """
        Validates:
        - Number of slides
        - Slide titles
        - Number and content of items
        - Dynamic presence check
        """
        url = "https://httpbin.org/xml"
        res = requests.get(url)

        assert res.status_code == 200
        assert res.headers["Content-Type"] == "application/xml", "Wrong header"

        # pretty print of xml
        print(parseString(res.text).toprettyxml())

        # conversion of xml to json
        xml_data = xmltodict.parse(res.text)

        # pretty print of json
        print(json.dumps(xml_data, indent=4))

        slides = xml_data["slideshow"]["slide"]

        # Validations
        assert len(slides) == 2
        titles = [slide["title"] for slide in slides]
        print(titles)
        assert len(titles) == 2
        assert titles[0] == "Wake up to WonderWidgets!", "Wrong First title"
        assert titles[1] == "Overview", "Second title should be 'Overview'"

        # validate items
        items = []
        for slide in slides:
            item = slide.get("item", [])
            if isinstance(item, str):
                items.append(item)
            else:
                items.extend(item)

        print(items)
        assert len(items) == 3, "There should be 3 items"
        assert items[0]['em'] == "WonderWidgets"
        assert items[2]['em'] == "buys"

