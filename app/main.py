import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    """
    A decorator that caches function results based on positional arguments.
    """
    # Each decorated function gets its own unique storage dictionary
    storage = {}

    @functools.wraps(func)
    def wrapper(*args) -> Callable:
        # Since args is a tuple, it is immutable and can be used as a key
        if args in storage:
            print("Getting from cache")
            return storage[args]
        else:
            print("Calculating new result")
            result = func(*args)
            storage[args] = result
            return result
            
    return wrapper
