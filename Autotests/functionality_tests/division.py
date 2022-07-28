from emuns import ResponseEndpoints, ResponseStatusCode
from main import request_status_code, request_result


def test_div_valid_values():
    assert request_result(ResponseEndpoints.division, 20, 10) == 2


def test_div_min_value():
    assert request_result(ResponseEndpoints.division, -2147483648, 2) == -1073741824


def test_div_max_values():
    assert request_result(ResponseEndpoints.division, 2147483647, 2147483647) == 1


def test_div_min_values():
    assert request_result(ResponseEndpoints.division, -2147483648, -2147483648) == 1


def test_div_min_plus_1():
    assert request_result(ResponseEndpoints.division, -2147483647, 1) == -2147483647


def test_div_min_minus_1():
    assert request_status_code(ResponseEndpoints.division, -2147483649, 1) == ResponseStatusCode.large_value_error.value


def test_div_max_minus_1():
    assert request_result(ResponseEndpoints.division, 2147483646, 1) == 2147483646


def test_div_max_plus_1():
    assert request_status_code(ResponseEndpoints.division, 2147483648, 1) == ResponseStatusCode.large_value_error.value


def test_div_zero_value():
    assert request_result(ResponseEndpoints.division, 0, 10) == 0


def test_div_by_zero_value():
    assert request_status_code(ResponseEndpoints.division, 3467, 0) == ResponseStatusCode.calculate_error.value


def test_div_fractional_number():
    assert request_status_code(ResponseEndpoints.division, 1.7, 10) == ResponseStatusCode.not_integer_error.value


def test_div_empty_value():
    assert request_status_code(ResponseEndpoints.division, "", 111) == ResponseStatusCode.not_integer_error.value


def test_div_str():
    assert request_status_code(ResponseEndpoints.division, "abc", 10) == ResponseStatusCode.not_integer_error.value
