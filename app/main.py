from typing import Any


def cache(func: Any) -> Any:
    cache_update = {}

    def wrapper(*args: Any) -> Any:
        if args in cache_update:
            print("Getting from cache")
            return cache_update[args]

        else:
            result = func(*args)
            cache_update[args] = result
            print("Calculating new result")
            return result

    return wrapper
