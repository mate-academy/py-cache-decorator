from typing import Callable


def cache(func: Callable) -> Callable:
    _cache = dict()

    def wrapper(*args: dict) -> dict:
        if args in _cache:
            print("Getting from cache")
            return _cache[args]
        print("Calculating new result")
        result = func(*args)
        _cache[args] = result
        return result

    return wrapper
