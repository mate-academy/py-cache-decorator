from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    storage = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in storage:
            print("Getting from cache")
            return storage[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        storage[cache_key] = result
        return result

    return wrapper
