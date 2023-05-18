from typing import Callable, Any


def cache(func: Callable) -> Any:
    saved_cache = dict()

    def inner(*args) -> Any:
        if isinstance(args, (dict, set, list)) is False:
            if args in saved_cache:
                print("Getting from cache")
                return saved_cache[args]
            result = func(*args)
            saved_cache[args] = result
            print("Calculating new result")
            return result
    return inner
