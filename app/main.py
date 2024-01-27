from typing import Callable
from functools import wraps

def cache(func: Callable) -> Callable:
    caching_result = {}
    @wraps(func)
    def wrapper(*args) -> Callable:
        if args in caching_result:
            print("Getting from cache")
            return caching_result[args]
        print("Calculating new result")
        caching_result[args] = func(*args)
        return caching_result[args]
    return wrapper
