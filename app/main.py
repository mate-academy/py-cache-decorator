from typing import Callable, Any


def cache(func: Callable) -> Any:
    cached = {}

    def inner(*args) -> Any:
        if args in cached:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached[args] = func(*args)
        return cached[args]

    return inner

#
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
# long_time_func_2((5, 6, 7), 5)
# long_time_func(1, 2, 3)
# long_time_func_2((5, 6, 7), 10)
# long_time_func_2((5, 6, 7), 10)
