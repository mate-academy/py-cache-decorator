from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cash_dict = {}

    @wraps(func)
    def inner(*args) -> Any:
        if args in cash_dict:
            print("Getting from cache")
            result = cash_dict[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cash_dict[args] = result
        return result

    return inner
