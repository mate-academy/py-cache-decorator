from functools import wraps
from collections.abc import Callable


def cache(func: Callable) -> Callable:
    store = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        if args in store.keys():
            print("Getting from cache")
            return store[args]
        maintain = func(*args, **kwargs)
        store[args] = maintain
        print("Calculating new result")
        return maintain

    return wrapper
