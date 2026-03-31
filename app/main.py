from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage: dict = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in storage:
            print("Getting from cache")
            return storage[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        storage[key] = result
        return result

    return wrapper
