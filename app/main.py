import functools
from typing import Callable, Any

def cache(func: Callable):
    area_cache = {}
    @functools.wraps(func)
    def wrap_cache(*args, **kwargs)-> Any:
        key = args + tuple(kwargs.values())
        if key in area_cache:
            print("Getting from cache")
            return area_cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            area_cache[key] = result
            return result
    return wrap_cache



@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]



