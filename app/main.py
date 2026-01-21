from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}
    def wrapper(*args, **kwargs) -> Callable:
        key = tuple(args) + tuple(sorted(kwargs.items()))
        if key  in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            print("Calculating new result")
            new_result = func(*args, **kwargs)
            cache_dict[key] = new_result
            return cache_dict[key]
    return wrapper

@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]




