from typing import Callable


def cache(func: Callable) -> Callable:
    data_dict = {}

    def inner(*args) -> Callable:
        if args in data_dict:
            print("Getting from cache")
            return data_dict[args]
        else:
            print("Calculating new result")
            data_dict[args] = func(*args)
            return data_dict[args]
    return inner


@cache
def long_time_func(var_a: int, var_b: int, var_c: int) -> int:
    return (var_a ** var_b ** var_c) % (var_a * var_c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
