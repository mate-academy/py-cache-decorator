from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    @wraps(func)
    def inner(*args) -> Any:
        if not storage or args not in storage:
            print("Calculating new result")
            storage[args] = func(*args)
        else:
            print("Getting from cache")
        return storage[args]
    return inner
