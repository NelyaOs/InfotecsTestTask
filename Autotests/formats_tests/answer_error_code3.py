from emuns import ResponseEndpoints, ResponseStatusCode, ResponseTextError
from main import request_json


def test_div_fractional_number():
    assert request_json(ResponseEndpoints.division, 34.67, 23) == {
        "statusCode": ResponseStatusCode.not_integer_error.value,
        "statusMessage": ResponseTextError.not_integer_error.value
    }
