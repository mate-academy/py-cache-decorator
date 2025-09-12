from typing import Callable, Any

_MISSING = object()


def cache(func: Callable) -> Callable:
    cached_result = {}

    def wrapper(*args) -> Any:
        result = cached_result.get(args, _MISSING)
        if result is not _MISSING:
            print("Getting from cache")
            return result
        print("Calculating new result")
        result = func(*args)
        cached_result[args] = result
        return result
    return wrapper
