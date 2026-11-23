from typing import Callable, Any


def cache(func: Callable) -> Callable:
    saved_cache = {}

    def wrapper(*args, **kwagrs) -> Any:
        key = (args, tuple(sorted(kwagrs)))
        if key in saved_cache:
            print("Getting from cache")
            return saved_cache[key]
        else:
            result = func(*args, **kwagrs)
            saved_cache[key] = result
            print("Calculating new result")
            return result

    return wrapper
