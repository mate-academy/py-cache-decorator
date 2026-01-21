from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    result = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any | None:
        key = (*args, tuple(sorted(kwargs.items())))
        if key not in result:
            result[key] = func(*args, **kwargs)
            print("Calculating new result")
            return result[key]
        else:
            print("Getting from cache")
            return result[key]
    return wrapper


@cache
def long_time_func(num1: int, num2: int, num3: int) -> int:
    return (num1 ** num2 ** num3) % (num1 * num3)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list[Any]:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
