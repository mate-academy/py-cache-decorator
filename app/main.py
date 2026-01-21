from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:

    cache_storage = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> any:
        key = (args, tuple(kwargs.items()))
        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_storage[key] = result
        return result
    return wrapper


@cache
def long_time_func(num_a: int, num_b: int, num_c: int) -> int:
    return (num_a ** num_b ** num_c) % (num_a * num_c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
