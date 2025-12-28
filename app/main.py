from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache = {}

    @wraps(func)
    def inner(*args: Any, **kwargs: Any) -> Any:
        key_result = (args, tuple(kwargs.values()), func.__name__)
        if key_result in cache:
            print("Getting from cache")
        else:
            cache[key_result] = func(*args, **kwargs)
            print("Calculating new result")
        return cache[key_result]
    return inner
