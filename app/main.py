from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cash_result = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        cash_key = tuple(args)
        if cash_key in cash_result:
            print("Getting from cache")
            return cash_result[cash_key]

        result = func(*args, **kwargs)
        cash_result[cash_key] = result
        print("Calculating new result")
        return result

    return wrapper
