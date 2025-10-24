from typing import Callable, Any


def cache(func: Callable) -> Callable:
    _cache: dict[tuple, Any] = {}

    def wrapper(*args) -> Any:
        if args in _cache:
            print("Getting from cache")
            return _cache[args]
        else:
            print("Calculating new result")
            result = func(*args)
            _cache[args] = result
            return result

    return wrapper
