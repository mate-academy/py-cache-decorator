from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cache_data = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items()))) 
        if key in cache_data:
            print("Getting from cache")
            return cache_data[key]
        else:
            print("Calculating new result")
            results = func(*args, **kwargs)
            cache_data[key] = results 
        return results
    return wrapper