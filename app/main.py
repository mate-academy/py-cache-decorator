from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    storage = {}

    @wraps(func)
    def wrapper(*args) -> Any:

        if args not in storage:
            print("Calculating new result")
            result_of_func = func(*args)
            storage[args] = result_of_func

        else:
            print("Getting from cache")

        return storage[args]

    return wrapper
