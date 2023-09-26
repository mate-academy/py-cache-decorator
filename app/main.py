from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args) -> Any:
        if args in cached_results:
            print("Getting from cache")
            return cached_results[args]
        result = func(*args)
        cached_results[args] = result
        print("Calculating new result")
        return result

    return wrapper
