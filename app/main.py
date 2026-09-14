from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cached = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key not in cached:
            cached[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return cached[key]

    return wrapper
