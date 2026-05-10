from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:

    stored_data = {}

    @wraps(func)
    def inner(*args) -> Any:

        if args not in stored_data:
            stored_data[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return stored_data[args]

    return inner
