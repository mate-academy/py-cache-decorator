from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        serialized_args = str(args) + str(kwargs)

        if serialized_args not in cached_results:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_results[serialized_args] = result
        else:
            print("Getting from cache")

        return cached_results[serialized_args]

    return wrapper
