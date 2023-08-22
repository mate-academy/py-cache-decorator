from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    result_args_dict = {}

    @wraps(func)
    def inner(*args) -> Any:
        if args in result_args_dict:
            print("Getting from cache")
        else:
            result_args_dict[args] = func(*args)
            print("Calculating new result")
        return result_args_dict[args]
    return inner
