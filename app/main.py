from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    saved = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if args in saved:
            print("Getting from cache")
            return saved[args]
        else:
            saved[args] = func(*args, **kwargs)
            print("Calculating new result")
            return saved[args]
    return wrapper


@cache
def long_time_func(a_arg: int, b_arg: int, c_arg: int) -> int:
    return (a_arg ** b_arg ** c_arg) % (a_arg * c_arg)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
