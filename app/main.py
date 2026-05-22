from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    results_dict = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        key = args
        if key not in results_dict:
            results_dict[key] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return results_dict[key]

    return wrapper


@cache
def long_time_func(num1: int, num2: int, num3: int) -> int:
    result = (num1 ** num2 ** num3) % (num1 * num3)
    return result


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
