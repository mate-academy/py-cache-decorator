from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable[..., Any]:
    cache_date = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = args + tuple(sorted(kwargs.items()))
        if key in cache_date:
            print("Getting from cache")
            return cache_date[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_date[key] = result
        return result

    return wrapper


@cache
def long_time_func(base: int, exponent: int, modulo: int) -> int:
    return (base ** exponent ** modulo) % (base * modulo)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]

# Refresh trigger for Mate
