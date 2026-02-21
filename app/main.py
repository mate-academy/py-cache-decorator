from typing import Callable, Any


def cache(func: Callable) -> Callable:
    existing_args = {}
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(kwargs.items()))
        if key in existing_args:
            print("Getting from cache")
        if key not in existing_args:
            existing_args[key] = func(*args, **kwargs)
            print("Calculating new result")
        return existing_args[key]
    return wrapper
