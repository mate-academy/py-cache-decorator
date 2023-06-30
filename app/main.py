from typing import Callable
from functools import wraps


def cache(func):
    dictionary_with_result = {}

    @wraps(func)
    def check_cache_calls(*args):
        if func.__name__ not in dictionary_with_result:
            dictionary_with_result[func.__name__] = {}

        if args in dictionary_with_result[func.__name__]:
            print("Getting from cache")
            return dictionary_with_result[func.__name__][args]
        else:
            result = func(*args)
            dictionary_with_result[func.__name__][args] = result
            print(dictionary_with_result)
            print("Calculating new result")
            print(result)
            return result

    return check_cache_calls


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return sum([number ** power for number in n_tuple])


long_time_func(1, 2, 3)
