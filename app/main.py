from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:

    dic_stor = {}

    @wraps(func)
    def wrapper(*args: any, **kwargs: any) -> any:
        key = (args, tuple(kwargs.items()))
        if key in dic_stor:
            print("Getting from cache")
            return dic_stor[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            dic_stor[key] = result
            return result
    return wrapper


@cache
def long_time_func(arg_a: int, arg_b: int, arg_c: int) -> int:
    return (arg_a ** arg_b ** arg_c) % (arg_a * arg_c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
