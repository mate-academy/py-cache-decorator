from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args) -> dict:
        if args in results:
            print("Getting from cache")
            return results[args]
        else:
            print("Calculating new result")
            result = func(*args)
            results[args] = result
            return result

    return wrapper


@cache
def long_time_func(first_num: int, second_num: int, third_num: int) -> int:
    return (first_num ** second_num ** third_num) % (first_num * third_num)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
