import requests

try:

    def test_wrong_regulation():
        url = 'https://api.dev.singlerulebook.com/srb_v0/content?jurisdiction=eu&regulation=aifmd'
        AUTH_HEADERS = {
            'Authorization': 'Bearer eyJraWQiOiJcL3BiSWxxcExuUUFiVHZcL0x5U04rTEttSEJlbXQ4QTRFTDVFd0JJTjZHc009IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI2ODQ4NmJlMy01NzBlLTQ1NjQtOGM1My05M2VmZTkwZTAyM2IiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmV1LXdlc3QtMS5hbWF6b25hd3MuY29tXC9ldS13ZXN0LTFfNUNtSklmeXFjIiwiY29nbml0bzp1c2VybmFtZSI6IjY4NDg2YmUzLTU3MGUtNDU2NC04YzUzLTkzZWZlOTBlMDIzYiIsImdpdmVuX25hbWUiOiJWaXZlayIsImF1ZCI6ImY3MDNiYWUyajhsMjJtaGFpMjdzZ2VjMzciLCJldmVudF9pZCI6IjFhNmE0ODZjLWM5NjYtNDg4YS1iNzQ5LWRkNGJmOTIzN2M5NiIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjY0NDI4MzIzLCJjdXN0b206ZW50aXR5X2lkIjoiMDAwMCIsImV4cCI6MTY2NDQzNDg2MCwiaWF0IjoxNjY0NDMxMjYwLCJmYW1pbHlfbmFtZSI6IkdhcmciLCJlbWFpbCI6InZpdmVrLmdhcmdAc2luZ2xlcnVsZWJvb2suY29tIn0.m5o9rD-BV_cdPtw59jGggKSQ7x0tnmwmam-zciRVq5LRdDaovx0_WRUp8tr28Pvv0ZncxUhLcHx47fjsdpN1TR-pCeQ4AG8v3mNlPDD-6En0eWsj882U45lZ9BPc1QhVo9mxjjw3S1yLHiyHuMsUjDkwKp9t8-BzL7bK9_GOUJQ8dxvq7xZHfAcDGQeaIUE1QCBd7JccP_h3aMb-12WQcHjUsISCKQWo3an6vu3IZDMkAIi7IBSTfkKDkAX2f8-Xw4mq9Hdoa_GvkCGtjTNAAROWYBhhq5xm-N03LpHhLX_DM1pmORMMO4UaxckYfi23ayeuA06sZiAE20BZIRv92g',
            'Content-Type': 'application/json', 'Origin': 'https://dev.singlerulebook.com'}
        response = requests.get(url=url, headers=AUTH_HEADERS)
        response_json = response.json()
        print(response_json)
        assert response.status_code != 401, "Invalid credentials"
        assert response.status_code != 403, "Access denied"
        assert response.status_code != 500, "Server is down"
        print(response_json)
        assert response.status_code == 200, 'Status Code is  200'
        tocs = response_json.get('toc')
        for toc in tocs:
            heading = toc.get('heading')
            assert heading == 'EU', 'Jurisdiction is matching'
        # assert response.status_code == 400, 'Error code for Bad request '
        # error_message = response_json.get('error_message')
        # assert error_message == 'Not found'
except AssertionError as msg:
    print(msg)
