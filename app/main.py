from typing import Callable

def cache(func: Callable) -> Callable:
    """A simple caching decorator."""

    cached_results = {}
    def wrapper(*args):
        if args in cached_results:
            print ("Getting from cache")
            result = cached_results[args]
        else:
            print ("Calculating new result")
            result = func(*args)
            cached_results[args] = result
        return result

    return wrapper

