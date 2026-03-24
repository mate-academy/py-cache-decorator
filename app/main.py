from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    result = {}

    @functools.wraps(func)
    def wrapper(*args) -> Any:
        if args in result:
            print("Getting from cache")
            return result[args]
        else:
            print("Calculating new result")
            res = func(*args)
            result[args] = res
            return res
    return wrapper
