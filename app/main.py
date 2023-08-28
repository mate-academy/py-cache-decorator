from typing import Callable


def cache(func: Callable) -> Callable:
    cache_results = {}

    def wrapper(*args, **kwargs) -> Callable:
        if args in cache_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_results[args] = func(*args, **kwargs)
        return cache_results[args]
    return wrapper


@cache
def long_time_func(number_1: int, number_2: int, number_3: int) -> int:
    return (number_1 ** number_2 ** number_3) % (number_1 * number_3)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
