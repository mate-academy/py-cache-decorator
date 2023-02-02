from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    dict__ = dict()

    @wraps(func)
    def inner(*args) -> Any:
        nonlocal dict__

        if not dict__.get((*args, inner.__name__,)) is None:
            print("Getting from cache")
            return dict__.get((*args, inner.__name__,))
        print("Calculating new result")

        dict__[(*args, inner.__name__,)] = func(*args)
        return dict__[(*args, inner.__name__,)]

    return inner
