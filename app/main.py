import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_calculations = {}

    @functools.wraps(func)
    def inner(*args) -> Any:
        if args not in stored_calculations:
            print("Calculating new result")
            result = func(*args)
            stored_calculations[args] = result
        else:
            print("Getting from cache")
        return stored_calculations[args]
    return inner
