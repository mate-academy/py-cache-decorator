from typing import Callable


def cache(func: Callable) -> Callable:
    input_data = {}

    def inner(*args, **kwargs) -> Callable:
        nonlocal input_data
        if args in input_data:
            print("Getting from cache")
            return input_data[args]
        else:
            input_data.update({args: func(*args)})
            print("Calculating new result")
            return input_data[args]
    return inner


# @cache
# def long_time_func(a, b, c):
#     return (a ** b ** c) % (a * c)
#
#
# @cache
# def long_time_func_2(n_tuple, power):
#     return [number ** power for number in n_tuple]
#
#
# long_time_func(1, 2, 3)
# long_time_func(2, 2, 3)
# long_time_func_2((3, 4, 5), 2)
# long_time_func(1, 2, 3)
# long_time_func_2((5, 6, 7), 10)
# long_time_func_2((5, 6, 7), 10)
