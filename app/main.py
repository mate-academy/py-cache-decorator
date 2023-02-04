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
def long_time_func(var_a: int, var_b: int, var_c: int) -> int:
    return (var_a ** var_b ** var_c) % (var_a * var_c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
