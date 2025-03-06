from typing import Callable, List
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:

        key = (func.__name__, args, frozenset(kwargs.items()))

        if key not in cache_dict:
            print("Calculating new result")
            cache_dict[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cache_dict[key]

    return wrapper


@cache
def long_time_func(abd: int, bas: int, cab: int) -> int:
    return (abd ** bas ** cab) % (abd * cab)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> List[int]:
    return [number ** power for number in n_tuple]
