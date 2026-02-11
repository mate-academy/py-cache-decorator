from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cached_results = {}
    @functools.wraps(func)
    def inner(*args) -> Callable:
        if args not in cached_results:
            print("Calculating new result")
            result = func(*args)
            cached_results[args] = result
        else:
            print("Getting from cache")
            result = cached_results[args]
        return result
    return inner

@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)