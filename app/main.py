from typing import Callable, Any


def cache(func: Callable) -> Any:
    stocked_cache = {}

    def inner(*args) -> int:
        if args not in stocked_cache:
            stocked_cache[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return stocked_cache[args]
    return inner
