from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = dict()

    @wraps(func)
    def wrapper(*args) -> Any:
        name_of_function = func.__name__
        if name_of_function not in cache_dict:
            cache_dict[name_of_function] = dict()
        if args not in cache_dict[name_of_function]:
            cache_dict[name_of_function][args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_dict[name_of_function][args]

    return wrapper
