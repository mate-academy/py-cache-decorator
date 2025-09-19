from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if not hasattr(wrapper, "_cache"):
            wrapper._cache = {}

        key = (args, tuple(sorted(kwargs.items())))

        if key in wrapper._cache:
            print("Getting from cache")
            return wrapper._cache[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        wrapper._cache[key] = result
        return result

    return wrapper
