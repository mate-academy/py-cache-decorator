import functools
from typing import Callable, Any


def cache(func) -> Callable:
    result_dict = {}

    @functools.wraps(func)
    def wrapper(*args) -> Any:
        if args not in result_dict:
            value = func(*args)
            result_dict[args] = value
            print(f"Calculating new result")
        else:
            print(f"Getting from cache")
        return result_dict[args]

    return wrapper
