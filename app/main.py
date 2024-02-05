from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    stored_results = {}

    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in stored_results.keys():
            print("Getting from cache")
            return stored_results[args]
        else:
            print("Calculating new result")
            new_value = func(*args)
            stored_results[args] = new_value
            return new_value
    return wrapper
