from typing import Callable


def cache(func: Callable) -> Callable:
    store_results = {}

    def inner(*args, **kwargs) -> any:
        key = (args, tuple(kwargs.items()))
        if key not in store_results:
            store_results[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return store_results[key]

    return inner


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
