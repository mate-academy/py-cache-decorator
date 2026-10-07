from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    saved_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        key = (args, tuple(sorted(kwargs.items())))

        if key in saved_results:
            print("Getting from cache")
            return saved_results[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        saved_results[key] = result

        return result

    return wrapper
