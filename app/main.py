from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        serialized_args = str(args) + str(kwargs)

        if serialized_args in cached_results:
            print("Getting from cache")
            return cached_results[serialized_args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_results[serialized_args] = result
            return result

    return wrapper
