from typing import Callable
from functools import wraps
from typing import Any


def cache(func: Callable) -> Callable:

    cache_dict = {}

    @wraps(func)
    def wrap(*args, **kwargs) -> Any:

        key = (args, frozenset(kwargs.items()))

        if key in cache_dict:
            print("Getting from cache")
            result = cache_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[key] = result
        return result

    return wrap
