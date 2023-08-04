from typing import Callable


def cache(func: Callable) -> Callable:
    runs_cache = {}

    def wrapper(*args) -> Callable:
        if args not in runs_cache.keys():
            runs_cache[args] = func(*args)
            print("Calculating new result")
            return runs_cache[args]
        else:
            print("Getting from cache")
            return runs_cache[args]

    return wrapper

#
# @cache
# def long_time_func(a: int, b: int, c: int) -> int:
#     return (a ** b ** c) % (a * c)
#
#
# @cache
# def long_time_func_2(n_tuple: tuple, power: int) -> int:
#     return [number ** power for number in n_tuple]
#
#
# long_time_func(1, 2, 3)
# long_time_func(2, 2, 3)
# long_time_func_2((5, 6, 7), 5)
# long_time_func(1, 2, 3)
# long_time_func_2((5, 6, 7), 10)
# long_time_func_2((5, 6, 7), 10)
#
# # Calculating new result
# # Calculating new result
# # Calculating new result
# # Getting from cache
# # Calculating new result
# # Getting from cache
