from typing import Callable, Any


def cache(func: Callable) -> Callable:
    unique_cash = {}

    def wrapper(*args: Any, **kwargs: Any) -> int:
        key = (args, tuple(kwargs))
        if key not in unique_cash:
            unique_cash[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return unique_cash[key]
    return wrapper
