from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Any:
    result = {}

    @wraps(func)
    def inner(*args: Any) -> Any:
        if args in result:
            print("Getting from cache")
            return result[args]
        else:
            result.update({args: func(*args)})
            print("Calculating new result")
        return result[args]

    return inner
