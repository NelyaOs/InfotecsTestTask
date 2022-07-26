import requests

def test_state():
    print(requests.get("http://localhost:5413/api/state").json())
    # assert (requests.get("http://localhost:5413/api/state")).json() == {'statusCode': 0, 'state': 'OК'}