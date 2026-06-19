from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage: dict[tuple[Any, ...], Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = args
        if kwargs:
            # kwargs order should not matter for key generation
            key = key + tuple(sorted(kwargs.items()))

        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_storage[key] = result
        return result

    return wrapper
