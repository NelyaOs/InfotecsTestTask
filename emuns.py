from enum import Enum

class ResponseStatusCode(Enum):
    ok = 0
    calculate_error = 1
    key_count_error = 2
    not_integer_error = 3
    large_value_error = 4
    wrong_format_error = 5

class ResponseEndpoints(Enum):
    addition = "addition"
    state = "state"
    multiplication = "multiplication"
    division = "division"
    remainder = "remainder"

class ResponseTextError(Enum):
    calculate_error = "Ошибка вычисления"
    key_count_error = "Не указаны необходимые параметры"
    not_integer_error = "Значения параметров должны быть целыми"
    large_value_error = "Превышены максимальные значения параметров"
    wrong_format_error = "Не допустимый формат json"