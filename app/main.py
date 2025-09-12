from typing import Callable


def cache(func: Callable) -> Callable:
    cached_result = {}
    def wrapper(*args, **kwargs):
        if args not in cached_result:
            cached_result[args] = func(*args, **kwargs)
            print("Calculating new result")
            return cached_result[args]
        else:
            print("Getting from cache")
        return cached_result[args]
    return wrapper