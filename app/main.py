from typing import Callable
from functools import wraps
from typing import Any


def cache(func: Callable) -> Callable:
    _cache = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in _cache:
            print("Getting from cache")
            return _cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            _cache[key] = result
            return result

    return wrapper


# Приклади функцій для тестування
@cache
def long_time_func(
        first_value: int,
        second_value: int,
        complexity: int
) -> int:
    return ((first_value ** second_value ** complexity)
            % (first_value * complexity))


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]


# Тестові виклики
if __name__ == "__main__":
    long_time_func(1, 2, 3)           # Calculating new result
    long_time_func(2, 2, 3)           # Calculating new result
    long_time_func_2((5, 6, 7), 5)    # Calculating new result
    long_time_func(1, 2, 3)           # Getting from cache
    long_time_func_2((5, 6, 7), 10)   # Calculating new result
    long_time_func_2((5, 6, 7), 10)   # Getting from cache
