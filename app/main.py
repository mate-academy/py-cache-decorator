from typing import Callable, Any


def cache(func: Callable) -> Any:
    saved_cache_dict = {}

    def inner(*args) -> Any:
        if isinstance(args, (dict, set, list)) is False:
            if args in saved_cache_dict:
                print("Getting from cache")
                return saved_cache_dict[args]
            result = func(*args)
            saved_cache_dict[args] = result
            print("Calculating new result")
            return result
    return inner
