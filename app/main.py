from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in result:
            print("Getting from cache")
            return result[args]
        result.update({args: func(*args)})
        print("Calculating new result")
        return result[args]

    return wrapper
