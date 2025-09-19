from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    stored_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if str([args, sorted(kwargs.items())]) in list(stored_cache.keys()):
            print("Getting from cache")
            return stored_cache[str([args, sorted(kwargs.items())])]
        stored_cache.update({str([args, sorted(kwargs.items())]): func(*args)})
        print("Calculating new result")
        return stored_cache[str([args, sorted(kwargs.items())])]
    return wrapper
