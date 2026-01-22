from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in results:
            print("Calculating new result")
            results[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return results[key]

    return wrapper
