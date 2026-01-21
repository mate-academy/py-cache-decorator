import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        if args in storage:
            print("Getting from cache")
            return storage[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            storage[args] = result
            return result            
    return wrapper
