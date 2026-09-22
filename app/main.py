from typing import Callable


def cache(func: Callable) -> Callable:
    _cache = {}

    def wrapper(*args) -> Callable:
        if args in _cache:
            print("Getting from cache")
            return _cache[args]
        else:
            print("Calculating new result")
            result = func(*args)
            _cache[args] = result
            return result
    return wrapper
