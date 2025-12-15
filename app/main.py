from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    dict_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        args_tuple = args + tuple(sorted(kwargs.items()))

        if args_tuple in dict_results:
            print("Getting from cache")
            return dict_results[args_tuple]
        else:
            result = func(*args, **kwargs)
            dict_results[args_tuple] = result
            print("Calculating new result")
            return result
    return wrapper
