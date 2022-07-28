from emuns import ResponseEndpoints, ResponseStatusCode
from main import request_json

okStatusCode = ResponseStatusCode.ok.value


def test_sum_valid_values():
    assert request_json(ResponseEndpoints.addition, 25, 142) == {"statusCode": okStatusCode, "result": 167}


def test_div_valid_values():
    assert request_json(ResponseEndpoints.division, 205, 5) == {"statusCode": okStatusCode, "result": 41}


def test_mult_valid_values():
    assert request_json(ResponseEndpoints.multiplication, 36, 4) == {"statusCode": okStatusCode, "result": 144}


def test_rem_valid_values():
    assert request_json(ResponseEndpoints.remainder, 20, 14) == {"statusCode": okStatusCode, "result": 6}
