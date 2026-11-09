from typing import Callable

def cache(func) -> Callable:
    cache = {}
    def cache_wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        if key in cache:
            print("Getting from cache")
            return cache[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return cache_wrapper
@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]

