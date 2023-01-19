from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    stored_functions = {}

    @functools.wraps(func)
    def inner(*args) -> Any:
        if args in stored_functions:
            print("Getting from cache")
        else:
            print("Calculating new result")
            stored_functions[args] = func(*args)
        return stored_functions[args]
    return inner
