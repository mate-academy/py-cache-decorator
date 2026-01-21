from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    saved_cache = {}

    def inner(*args) -> Any:
        key = args
        if key not in saved_cache:
            print("Calculating new result")
            result = func(*args)
            saved_cache[key] = result
            return result
        else:
            print("Getting from cache")
            return saved_cache[key]
    return inner
