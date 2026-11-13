from typing import Callable

def cache(func: Callable) -> Callable:
    cache_storage = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_storage[key] = result
        return result
    return wrapper



@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]