from typing import Callable


def cache(func: Callable) -> Callable:
    dict_for_res = {}

    def inner(*args, **kwargs) -> tuple:
        if args in dict_for_res:
            print("Getting from cache")
        else:
            dict_for_res[args] = func(*args)
            print("Calculating new result")
        return dict_for_res[args]
    return inner


@cache
def long_time_func(first_a: int, second_b: int, third_c: int) -> int:
    return (first_a ** second_b ** third_c) % (first_a * third_c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
