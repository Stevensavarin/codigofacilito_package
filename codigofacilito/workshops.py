import requests

def unreleased():
    response = requests.get("https://dummyjson.com/quotes")

    if response.status_code == 200:
        payload = response.json()
        return payload["quotes"]