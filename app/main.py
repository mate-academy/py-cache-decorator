from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:

    cash = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> int | Any:
        if f"{func}, {args}" in cash:
            print("Getting from cache")
            return cash[f"{func}, {args}"]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cash[f"{func}, {args}"] = result
        return result
    return wrapper
