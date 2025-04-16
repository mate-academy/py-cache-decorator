from typing import Callable


def cache(func: Callable) -> Callable:
    _cache = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key in _cache:
            print("Getting from cache")
            return _cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            _cache[key] = result
            return result

    return wrapper
