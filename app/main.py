from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args) -> Callable:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]

        res = func(*args)
        cache_dict[args] = res
        print("Calculating new result")
        return res

    return inner


@cache
def long_time_func(num1: int, num2: int, num3: int) -> int:
    return num1 * num2 * num3


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number**power for number in n_tuple]
