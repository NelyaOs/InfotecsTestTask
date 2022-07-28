from emuns import ResponseEndpoints, ResponseStatusCode, ResponseTextError
from main import request_wrong_format_error


def test_format_error():
    assert request_wrong_format_error(ResponseEndpoints.addition, 25, 48) == {
        "statusCode": ResponseStatusCode.wrong_format_error.value,
        "statusMessage": ResponseTextError.wrong_format_error.value
    }
