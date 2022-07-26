from emuns import ResponseEndpoints, ResponseStatusCode
from main import request_status_code, request_result


def test_rem_valid_values():
    assert request_result(ResponseEndpoints.remainder, 20, 14) == 6

def test_rem_max_and_min_values():
    assert request_result(ResponseEndpoints.remainder, -2147483648, 2147483647) == 2147483646

def test_rem_max_values():
    assert request_result(ResponseEndpoints.remainder, 2147483647, 2147483647) == 0

def test_rem_max_minus_1():
    assert request_result(ResponseEndpoints.remainder, 2147483646, 10) == 6

def test_rem_max_plus_1():
    assert request_status_code(ResponseEndpoints.remainder, 2147483648, 10) == ResponseStatusCode.large_value_error.value

def test_rem_min_values():
    assert request_result(ResponseEndpoints.remainder, -2147483648, -2147483648) == 0

def test_rem_min_plus_1():
    assert request_result(ResponseEndpoints.remainder, -2147483647, 10) == 3

def test_rem_min_minus_1():
    assert request_status_code(ResponseEndpoints.remainder, -2147483649, 10) == ResponseStatusCode.large_value_error.value

def test_rem_by_zero_value():
    assert request_status_code(ResponseEndpoints.remainder, 15, 0) == ResponseStatusCode.calculate_error.value

def test_rem_zero_value():
    assert request_result(ResponseEndpoints.remainder, 0, 15) == 0

def test_rem_smaller_by_the_larger():
    assert request_result(ResponseEndpoints.remainder, 3, 15) == 3

def test_rem_fractional_number():
    assert request_status_code(ResponseEndpoints.remainder, 1.7, 10) == ResponseStatusCode.not_integer_error.value

def test_rem_empty_value():
    assert request_status_code(ResponseEndpoints.remainder, "", 111) == ResponseStatusCode.not_integer_error.value

def test_rem_str():
    assert request_status_code(ResponseEndpoints.remainder, "abc", 10) == ResponseStatusCode.not_integer_error.value


