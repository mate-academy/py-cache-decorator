from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached = dict()

    @wraps(func)
    def wrapped(*args) -> Any:
        if args in cached:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached[args] = func(*args)

        return cached[args]

    return wrapped
