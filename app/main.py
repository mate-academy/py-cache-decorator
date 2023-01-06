from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        dict_key = args + tuple(kwargs.items())
        if dict_key not in wrapper.cache:
            wrapper.cache[dict_key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return wrapper.cache[dict_key]

    wrapper.cache = {}
    return wrapper


@cache
def long_time_func(data_a: int, data_b: int, data_c: int) -> Any:
    return (data_a ** data_b ** data_c) % (data_a * data_c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> Any:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
