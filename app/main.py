from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if args not in result:
            result.update({args: func(*args)})
            print("Calculating new result")
        else:
            print("Getting from cache")
        return result[args]
    return wrapper
