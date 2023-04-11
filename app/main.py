from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_args = {}

    def wrapper(*args, **kwargs) -> Any:
        key = args
        if key in cache_args:
            print("Getting from cache")
            return cache_args[key]
        cache_args[key] = func(*args, **kwargs)
        print("Calculating new result")
        return cache_args[key]
    return wrapper


# @cache
# def long_time_func(a: int, b: int, c: int) -> int:
#     return (a ** b ** c) % (a * c)
#
#
# @cache
# def long_time_func_2(n_tuple: tuple, power: int) -> Any:
#     return [number ** power for number in n_tuple]
#
#
# long_time_func(1, 2, 3)
# long_time_func(2, 2, 3)
# long_time_func_2((5, 6, 7), 5)
# long_time_func(1, 2, 3)
# long_time_func_2((5, 6, 7), 10)
# long_time_func_2((5, 6, 7), 5)
# long_time_func_2((5, 6, 7), 10)
