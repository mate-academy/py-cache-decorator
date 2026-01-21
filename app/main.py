from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    stored_caches = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        try:
            cache_keys = (args, tuple(sorted(kwargs.items())))
        except TypeError:
            print("Calculating new result")
            return func(*args, **kwargs)

        if cache_keys in stored_caches:
            print("Getting from cache")
            return stored_caches[cache_keys]
        print("Calculating new result")
        result = func(*args, **kwargs)
        stored_caches[cache_keys] = result
        return result
    return wrapper


@cache
def long_time_func(var_a: int, var_b: int, var_c: int) -> int:
    return (var_a ** var_b ** var_c) % (var_a * var_c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
