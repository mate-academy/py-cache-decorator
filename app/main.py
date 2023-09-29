from typing import Callable


def cache(func: Callable) -> Callable:
    cached_data = {}

    def inner(*args, **kwargs):
        if args in cached_data.keys():
            print("Getting from cache")
        else:
            new_cache = func(*args)
            cached_data[args] = new_cache
            print("Calculating new result")

        return func(*args) if args not in cached_data.keys() else cached_data[args]

    return inner

@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
