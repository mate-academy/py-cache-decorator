import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    store = {}

    @functools.wraps(func)
    def inner(*args: Any) -> str:
        if args not in store:
            store.update({args: func(*args)})
            print("Calculating new result")
        else:
            print("Getting from cache")
        return store[args]
    return inner
