from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cache_update = {}

    def wrapper(*args: Any) -> Any:
        if args in cache_update:
            print("Getting from cache")
        else:
            result = func(*args)
            cache_update[args] = result
            print("Calculating new result")

        return cache_update[args]

    return wrapper
