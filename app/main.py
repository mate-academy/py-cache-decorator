
from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key not in results:
            results[key] = func(*args, **kwargs)

        return results[key]

    return wrapper
