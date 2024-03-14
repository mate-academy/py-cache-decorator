from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cash_result = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        cash_key = tuple(args)
        if cash_key in cash_result:
            print("Getting from cache")
        else:
            cash_result[cash_key] = func(*args, **kwargs)
            print("Calculating new result")
        return cash_result[cash_key]

    return wrapper
