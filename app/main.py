from typing import Any, Hashable, Callable


def cache(func: Callable) -> Callable:
    cache_stored = dict()

    def wrapper(*args: Hashable) -> Any:
        if args in cache_stored:
            print("Getting from cache")
            return cache_stored[args]
        cache_stored[args] = func(*args)
        print("Calculating new result")
        return cache_stored[args]

    return wrapper
