from typing import Callable, Any, Dict, Tuple
import functools


def cache(func: Callable) -> Callable:
    cache_dict: Dict[Tuple, Any] = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = args

        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result
    return wrapper


@cache
def long_time_func(var1: int, var2: int, var3: int) -> int:
    return (var1 ** var2 ** var3) % (var1 * var3)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
