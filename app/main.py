from typing import Any, Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    dict_of_results = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        if args not in dict_of_results:
            print("Calculating new result")
            dict_of_results[args] = func(*args, **kwargs)
            return dict_of_results[args]
        print("Getting from cache")
        return dict_of_results[args]

    return inner
