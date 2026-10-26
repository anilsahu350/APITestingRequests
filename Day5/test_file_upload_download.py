import requests


class TestFileUploadDownload:
    BASE_URL = "http://localhost:8080"
    FILE1 = "C:/Automation/automationFiles/Test1.txt"
    FILE2 = "C:/Automation/automationFiles/Test2.txt"

    def test_upload_single_file(self):
        with open(self.FILE1, "rb") as file:
            files = {"file": file}
            res = requests.post(f"{self.BASE_URL}/uploadFile", files=files)
        assert res.status_code == 200, "Upload Failed"
        data = res.json()
        assert data['fileName'] == "Test1.txt", "Wrong file name"
        print(data)

    def test_upload_multiple_files(self):
        with open(self.FILE1, "rb") as f1, open(self.FILE2, "rb") as f2:
            files = [("files", f1), ("files", f2)]
            res = requests.post(f"{self.BASE_URL}/uploadMultipleFiles", files=files)
        assert res.status_code == 200, "Upload Failed"
        data = res.json()
        print(data)

    def test_download_file(self):
        filename = "Test1.txt"
        res = requests.get(f"{self.BASE_URL}/downloadFile/{filename}")
        assert res.status_code == 200, " wrong status code"
        output_path = f"downloaded_{filename}"
        with open(output_path, 'wb') as f:
            f.write(res.content)