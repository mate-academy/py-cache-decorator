from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Any:
    cash = {}

    @wraps(func)
    def wrapper(*args: tuple) -> Any:
        if args in cash:
            print("Getting from cache")
            return cash[args]
        else:
            print("Calculating new result")
        cash[args] = func(*args)
        return cash[args]
    return wrapper
