from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        print("Calculating new result")
        if not isinstance(args, (list, set, dict)):
            cache_dict[args] = func(*args)
        return cache_dict[args]

    return inner
