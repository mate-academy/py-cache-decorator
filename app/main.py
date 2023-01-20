from typing import Callable


def cache(func: Callable) -> Callable:
    cache_func = {}

    def wrapper(*args) -> Callable:
        if args in cache_func:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_func[args] = func(*args)
        return cache_func[args]
    return wrapper
