from emuns import ResponseEndpoints, ResponseStatusCode, ResponseTextError
from main import request_json

def test_large_value():
    assert request_json(ResponseEndpoints.addition, -2147483668, 10) == {"statusCode": ResponseStatusCode.large_value_error.value, "statusMessage": ResponseTextError.large_value_error.value}