from emuns import ResponseEndpoints, ResponseStatusCode, ResponseTextError
from main import request_json

def test_div_by_zero_value():
    assert request_json(ResponseEndpoints.division, 3467, 0) == {"statusCode": ResponseStatusCode.calculate_error.value, "statusMessage": ResponseTextError.calculate_error.value}