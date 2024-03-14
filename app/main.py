from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cashed_value = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        if args not in cashed_value:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cashed_value[args] = result
            return result
        print("Getting from cache")
        return cashed_value[args]
    return inner
