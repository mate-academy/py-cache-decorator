from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    stored_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in stored_results:
            print("Getting from cache")
            return stored_results[key]
        print("Calculating new result")
        stored_results[key] = func(*args, **kwargs)
        return stored_results[key]

    return wrapper


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
