from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    func_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        sorted_kwargs_tuple = tuple(sorted(kwargs.items()))
        cache_key = args + sorted_kwargs_tuple
        if cache_key in func_cache:
            print("Getting from cache")
            return func_cache[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            func_cache[cache_key] = result
            return result

    return wrapper


@cache
def long_time_func(number1: int, number2: int, number3: int) -> int:
    return (number1 ** number2 ** number3) % (number1 * number3)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
