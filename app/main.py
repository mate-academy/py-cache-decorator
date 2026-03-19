from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    result = {}

    @wraps(func)
    def inner(*args: Any, **kwargs: Any) -> Any:
        key = args
        if kwargs:
            key = args + tuple(sorted(kwargs.items()))

        try:
            if key in result:
                print("Getting from cache")
                return result[key]
            else:
                print("Calculating new result")
                result[key] = func(*args, **kwargs)
                return result[key]
        except TypeError:
            raise TypeError("Arguments must be hashable")

    return inner
