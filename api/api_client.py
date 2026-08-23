import requests
import urllib3
from config import BASE_URL, HEADERS, TIMEOUT, VERIFY_SSL

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class APIClient:
    #Reusable API helper class!
    def get(self, endpoint):
        #send GET request
        url = f"{BASE_URL}{endpoint}"
        response = requests.get(
            url,
            headers = HEADERS,
            timeout= TIMEOUT,
            verify= VERIFY_SSL
        )
        return response

    def post(self, endpoint, data):
        #send POST request (create new data)
        url =f"{BASE_URL}{endpoint}"
        response = requests.post(
            url,
            json=data,
            headers=HEADERS,
            timeout=TIMEOUT,
            verify=VERIFY_SSL
        )
        return response
    def put(self, endpoint, data):
        #send PUT request (update existing data)
        url=f"{BASE_URL}{endpoint}"
        response = requests.put(
            url,
            json=data,
            headers=HEADERS,
            timeout=TIMEOUT,
            verify=VERIFY_SSL
        )
        return response
    def delete(self, endpoint):
        #send DELETE request
        url=f"{BASE_URL}{endpoint}"
        response= requests.delete(
            url,
            headers=HEADERS,
            timeout=TIMEOUT,
            verify=VERIFY_SSL
        )
        return response