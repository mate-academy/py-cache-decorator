from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def create(*args) -> Any:
        try:
            hash(args)
        except TypeError:
            raise TypeError("Arguments must be immutable!")
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_dict[args] = result
            return result

    return create
