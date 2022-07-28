from emuns import ResponseEndpoints, ResponseStatusCode, ResponseTextError
from main import request_key_count_error

def test_key_count_error():
    assert request_key_count_error(ResponseEndpoints.multiplication, 15) == {"statusCode": ResponseStatusCode.key_count_error.value, "statusMessage": ResponseTextError.key_count_error.value}
