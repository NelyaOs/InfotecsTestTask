from emuns import ResponseEndpoints, ResponseStatusCode
from main import request_status_code, request_result, request_json



def test_sum_valid_values():
    assert request_json(ResponseEndpoints.addition, 25, 142) == {"statusCode": 0, "result": 167}

def test_div_valid_values():
    assert request_json(ResponseEndpoints.division, 205, 5) == {"statusCode": 0, "result": 41}

def test_mult_valid_values():
    assert request_json(ResponseEndpoints.multiplication, 36, 4) == {"statusCode": 0, "result": 144}

def test_rem_valid_values():
    assert request_json(ResponseEndpoints.remainder, 20, 14) == {"statusCode": 0, "result": 6}