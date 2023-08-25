from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    result_dict = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args not in result_dict.keys():
            print("Calculating new result")
            result_dict[args] = func(*args)
        else:
            print("Getting from cache")

        return result_dict[args]

    return wrapper
