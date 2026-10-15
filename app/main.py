from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    storage = {}

    def inner(*args) -> Any:
        if args in storage:
            print("Getting from cache")
            return storage[args]
        else:
            print("Calculating new result")
            result = func(*args)
            storage[args] = result
            return result
    return inner
