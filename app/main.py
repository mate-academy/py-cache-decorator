from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    my_cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))
        if key in my_cache:
            print("Getting from cache")
            return my_cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            my_cache[key] = result
        return my_cache[key]
    return wrapper


@cache
def long_time_func(anny: int, beny: int, ceny: int) -> int:
    return (anny ** beny ** ceny) % (anny * ceny)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


long_time_func_2((5, 6, 7), 5)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func(1, 2, 3)
