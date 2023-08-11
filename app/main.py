from typing import Callable, Any


def cache(func: Callable) -> Callable:
    caches = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in caches:
            print("Getting from cache")
            return caches[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        caches[key] = result
        return result

    return wrapper
