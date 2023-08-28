from typing import Callable


def cache(func: Callable) -> Callable:
    cache_results = {}

    def wrapper(*args, **kwargs) -> Callable:
        if args in cache_results:
            print("Getting from cache")
            return cache_results[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_results[args] = result
        return result
    return wrapper


@cache
def long_time_func(number_1: int, number_2: int, number_3: int) -> int:
    return (number_1 ** number_2 ** number_3) % (number_1 * number_3)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
