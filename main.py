import requests

baseUrl = "http://localhost:5413/api/"


def request_result(endpoint, x, y):
    request = requests.post(baseUrl + endpoint.value, json={"x": x, "y": y})
    return request.json()['result']


def request_status_code(endpoint, x, y):
    request = requests.post(baseUrl + endpoint.value, json={"x": x, "y": y})
    return request.json()['statusCode']


def request_json(endpoint, x, y, ):
    request = requests.post(baseUrl + endpoint.value, json={"x": x, "y": y})
    return request.json()


def request_key_count_error(endpoint, x):
    request = requests.post(baseUrl + endpoint.value, json={"x": x})
    return request.json()


def request_wrong_format_error(endpoint, x, y):
    request = requests.post(baseUrl + endpoint.value, proxies={"x": x, "y": y})
    return request.json()
