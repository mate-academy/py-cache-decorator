from typing import Callable, Any


def cache(func: Callable) -> Callable:
    ul = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in ul:
            print("Getting from cache")
            return ul[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        ul[key] = result
        return result
    return wrapper
