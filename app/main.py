from typing import Callable


def cache(func: Callable) -> Callable:
    dict_cache = {}

    def wrapper(*args: Callable) -> Callable:
        if args in dict_cache:
            print("Getting from cache")
            return dict_cache[args]
        else:
            print("Calculating new result")
            dict_cache[args] = func(*args)
            return dict_cache[args]
    return wrapper


@cache
def long_time_func(num_1: int, num_2: int, num_3: int) -> int:
    return (num_1 ** num_2 ** num_3) % (num_1 * num_3)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
