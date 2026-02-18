from typing import Callable, Any


def cache(func: Callable) -> Callable:
    if not hasattr(func, "__cache__"):
        func.__cache__ = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in func.__cache__:
            print("Getting from cache")
            return func.__cache__[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        func.__cache__[key] = result
        return result

    return wrapper
