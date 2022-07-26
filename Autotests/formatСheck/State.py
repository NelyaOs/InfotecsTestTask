import requests

def test_state():
    assert (requests.get("http://localhost:5413/api/state")).json() == {'statusCode': 0, 'state': 'OК'}