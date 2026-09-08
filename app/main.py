from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))

        if key in stored_results:
            print("Getting from cache")
            return stored_results[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        stored_results[key] = result
        return result

    return wrapper


@cache
def long_time_func(base: int, exponent: int, divisor: int) -> int:
    return (base ** exponent ** divisor) % (base * divisor)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
