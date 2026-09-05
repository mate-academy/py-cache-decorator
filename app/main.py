from typing import Callable, Any


def cache(func: Callable) -> Callable:
    def inner(*args) -> Any:
        if args in inner.cache_dict:
            print("Getting from cache")
            return inner.cache_dict[args]
        else:
            print("Calculating new result")
            result = func(*args)
            inner.cache_dict[args] = result
            return result
    inner.cache_dict = {}
    return inner
