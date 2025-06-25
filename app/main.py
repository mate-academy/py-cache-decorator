from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    stored_cache: dict[Any, Any] = {}

    @wraps(func)
    def inner(*args) -> Any:
        if args in stored_cache:
            print("Getting from cache")
            return stored_cache[args]
        else:
            print("Calculating new result")
            result = func(*args)
            stored_cache[args] = result
            return result
    return inner
