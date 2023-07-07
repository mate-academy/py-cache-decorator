from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    @wraps(func)
    def inner(*args) -> int:
        if args not in storage:
            res = func(*args)
            storage.update({args: res})
            print("Calculating new result")
            return res

        print("Getting from cache")
        return storage[args]

    return inner
