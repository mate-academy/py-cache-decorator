from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    caching_place = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        arguments = args + tuple(sorted(kwargs.items()))
        if arguments in caching_place:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            caching_place[arguments] = result
        return caching_place[arguments]
    return wrapper
