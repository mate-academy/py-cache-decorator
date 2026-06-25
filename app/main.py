from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def make_key(args, kwargs):
        return (args, tuple(kwargs.items()))

    def wrapper(*args, **kwargs):
        key = make_key(args, kwargs)

        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[key] = result
        return result

    return wrapper


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * b)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
