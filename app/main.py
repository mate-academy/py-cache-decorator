import functools
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    storage_of_cache = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> Any:
        key = (args, func, tuple(kwargs.items()))
        if key not in storage_of_cache:
            print("Calculating new result")
            result = func(*args, **kwargs)
            storage_of_cache[key] = result
            return result
        else:
            print("Getting from cache")
            return storage_of_cache[key]
    return inner


@cache
def long_time_func(arg_a: int, arg_b: int, arg_c: int) -> int:
    return (arg_a ** arg_b ** arg_c) % (arg_a * arg_c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
