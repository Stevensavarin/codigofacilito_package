import requests

def unreleased():
    """Retorna diferentes quotes.

    >>> type(unreleased()) == type(list())
    True
    """
    response = requests.get("https://dummyjson.com/quotes")

    if response.status_code == 200:
        payload = response.json()
        return payload["quotes"]