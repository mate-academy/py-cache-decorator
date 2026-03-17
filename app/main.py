from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    storage: dict[tuple[Any, ...], Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (*args, tuple(sorted(kwargs.items())))
        if key in storage:
            print("Getting from cache")
            return storage[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        storage[key] = result
        return result

    return wrapper
