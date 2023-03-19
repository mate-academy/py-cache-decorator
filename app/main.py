from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    dict__ = {}

    @wraps(func)
    def inner(*args) -> Any:

        hash__ = hash(args)
        if not dict__.get(hash__) is None:
            print("Getting from cache")
        else:
            print("Calculating new result")
            dict__[hash__] = func(*args)

        return dict__[hash__]

    return inner
