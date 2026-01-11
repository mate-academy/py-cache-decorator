from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in results:
            print("Getting from cache")
            return results[key]
        else:
            print("Calculating new result")
            results[key] = func(*args, **kwargs)
            return results[key]

    return wrapper
