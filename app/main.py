from functools import wraps
from typing import Callable


def make_hashable_key(*args, **kwargs) -> tuple:
    args_tuple = tuple(args)
    kwargs_tuple = tuple(sorted(kwargs.items()))
    return (args_tuple, kwargs_tuple)


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = make_hashable_key(*args, **kwargs)
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[key] = result
        return result
    return wrapper


@cache
def long_time_func(vara: int, varb: int, varc: int) -> int:
    return (vara ** varb ** varc) % (vara * varc)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)

# Calculating new result
# Calculating new result
# Calculating new result
# Getting from cache
# Calculating new result
# Getting from cache
