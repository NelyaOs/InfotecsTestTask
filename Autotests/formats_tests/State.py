import requests

from main import baseUrl


def test_state():
    assert (requests.get(baseUrl + "state")).json() == {'statusCode': 0, 'state': 'OК'}
