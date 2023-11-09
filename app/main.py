from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_items = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args not in cached_items:
            print("Calculating new result")
            new_result = func(*args)
            cached_items[args] = new_result
            return new_result
        print("Getting from cache")
        return cached_items.get(args)
    return wrapper
