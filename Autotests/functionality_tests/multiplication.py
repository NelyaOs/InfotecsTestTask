from emuns import ResponseEndpoints, ResponseStatusCode
from main import request_status_code, request_result


def test_mult_valid_values():
    assert request_result(ResponseEndpoints.multiplication, 10, 2) == 20


def test_mult_zero_values():
    assert request_result(ResponseEndpoints.multiplication, 0, 0) == 0


def test_mult_negative_and_positive_values():
    assert request_result(ResponseEndpoints.multiplication, -10, 2) == -20


def test_mult_negative_values():
    assert request_result(ResponseEndpoints.multiplication, -10, -2) == 20


def test_mult_fractional_number():
    assert request_status_code(ResponseEndpoints.multiplication, 10.5, 2) == ResponseStatusCode.not_integer_error.value


def test_mult_min_value():
    assert request_result(ResponseEndpoints.multiplication, -2147483648, 2) == -4294967296


def test_mult_min_minus_1():
    assert request_status_code(ResponseEndpoints.multiplication, -2147483649,
                               2) == ResponseStatusCode.large_value_error.value


def test_mult_min_plus_1():
    assert request_result(ResponseEndpoints.multiplication, -2147483647, 2) == -4294967294


def test_mult_max_and_min_values():
    assert request_result(ResponseEndpoints.multiplication, -2147483648, 2147483647) == -4611686016279904256


def test_mult_max_value():
    assert request_result(ResponseEndpoints.multiplication, 2147483647, 2) == 4294967294


def test_mult_max_plus_1():
    assert request_status_code(ResponseEndpoints.multiplication, 2147483648,
                               2) == ResponseStatusCode.large_value_error.value


def test_mult_max_minus_1():
    assert request_result(ResponseEndpoints.multiplication, 2147483646, 2) == 4294967292


def test_mult_str():
    assert request_status_code(ResponseEndpoints.multiplication, "abc", 2) == ResponseStatusCode.not_integer_error.value


def test_mult_empty_value():
    assert request_status_code(ResponseEndpoints.multiplication, "", 2) == ResponseStatusCode.not_integer_error.value
