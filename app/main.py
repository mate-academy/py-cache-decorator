from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached = {}

    def inner(*args, **kwargs) -> Any:

        if args not in cached:
            new_cache = func(*args)
            cached[args] = new_cache
            print("Calculating new result")
        else:
            print("Getting from cache")

        return cached[args]

    return inner
