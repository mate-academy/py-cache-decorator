from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

       def wrapper(*args, **kwargs) -> dict:
        key = (args, frozenset(kwargs.items())) if kwargs else args
        if key not in cache_dict:
            cache_dict[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_dict[key]
           
    return wrapper
    pass
