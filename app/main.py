from typing import Callable
from functools import wraps
from typing import Any


def cache(func: Callable) -> Callable:
    results_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        sorted_kwargs = tuple(sorted(kwargs.items()))
        key = (args, sorted_kwargs)
        if key not in results_cache:
            print("Calculating new result")
            results_cache[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return results_cache[key]
    return wrapper
