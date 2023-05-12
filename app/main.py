from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = args + tuple(kwargs.items())
        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_results[key] = result
            return result

    return wrapper


@cache
def long_time_func(var1: int, var2: int, var3: int) -> int:
    return (var1 ** var2 ** var3) % (var1 * var3)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
