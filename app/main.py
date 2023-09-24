from typing import Callable


def cache(func: Callable) -> Callable:
    _cache = {}

    def decorator(*args, **kwargs) -> Callable:
        if args in _cache:
            print("Getting from cache")
            return _cache[args]
        else:
            res = func(*args)
            _cache[args] = res
            print("Calculating new result")
            return res
    return decorator
