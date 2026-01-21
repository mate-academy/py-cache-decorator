import functools
from typing import Callable


def cache(func: Callable) -> Callable:
   storage = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        # Since args is a tuple, it is immutable and can be used as a key
        if args in storage:
            print("Getting from cache")
            return storage[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            storage[args] = result
            return result            
    return wrapper
