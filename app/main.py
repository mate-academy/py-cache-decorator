import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_kwargs = {}

    @functools.wraps(func)
    def wrapper(*args) -> Any:

        if args in result_kwargs.keys():
            print("Getting from cache")
            return result_kwargs[args]
        else:
            print("Calculating new result")
            result = func(*args)
            result_kwargs[args] = result
            return result

    return wrapper
