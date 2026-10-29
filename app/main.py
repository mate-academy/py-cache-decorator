from typing import Callable


def cache(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Callable:
        if args not in wrapper.cache:
            print("Calculating new result")
            result = func(*args, **kwargs)
            wrapper.cache[args] = result
            return result
        else:
            print("Getting from cache")
            return wrapper.cache[args]
    wrapper.cache = {}
    return wrapper
