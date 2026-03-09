from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    storage = {}

    @wraps(func)
    def wrapper(*args: Callable, **kwargs: Callable) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))

        if key in storage:
            print("Getting from cache")
            return storage[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        storage[key] = result
        return result

    return wrapper


@cache
def long_time_func(base: int, exponent: int, power: int) -> int:
    return (base**exponent**power) % (base * power)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number**power for number in n_tuple]
