from emuns import ResponseEndpoints, ResponseStatusCode
from main import request_status_code, request_result


def test_sum_valid_values():
    assert request_result(ResponseEndpoints.addition, 20, 14) == 34

def test_sum_max_and_min_values():
    assert request_result(ResponseEndpoints.addition, -2147483648, 2147483647) == -1

def test_sum_max_values():
    assert request_result(ResponseEndpoints.addition, 2147483647, 2147483647) == 4294967294

def test_sum_min_values():
    assert request_result(ResponseEndpoints.addition, -2147483648, -2147483648) == -4294967296

def test_sum_min_plus_1():
    assert request_result(ResponseEndpoints.addition, -2147483647, 10) == -2147483637

def test_sum_min_minus_1():
    assert request_status_code(ResponseEndpoints.addition, -2147483649, 10) == ResponseStatusCode.large_value_error.value

def test_sum_max_minus_1():
    assert request_result(ResponseEndpoints.addition, 2147483646, -10) == 2147483636

def test_sum_max_plus_1():
    assert request_status_code(ResponseEndpoints.addition, 2147483648, -10) == ResponseStatusCode.large_value_error.value

def test_sum_zero_value():
    assert request_result(ResponseEndpoints.addition, 0, 10) == 10

def test_sum_fractional_number():
    assert request_status_code(ResponseEndpoints.addition, 1.7, 10) == ResponseStatusCode.not_integer_error.value

def test_sum_empty_value():
    assert request_status_code(ResponseEndpoints.addition, "", 111) == ResponseStatusCode.not_integer_error.value

def test_sum_str():
    assert request_status_code(ResponseEndpoints.addition, "abc", 10) == ResponseStatusCode.not_integer_error.value


