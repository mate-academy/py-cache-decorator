from typing import Callable, Any


def cache(func: Callable) -> Callable:
    _cache = dict()

    def wrapper(*args, **kwargs) -> Any:
        data = (args, tuple(kwargs.items()))

        if data in _cache:
            print("Getting from cache")
            return _cache[data]

        print("Calculating new result")
        result = func(*args, **kwargs)
        _cache[data] = result

        return result

    return wrapper
