from collections.abc import Hashable
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    def inner(*args: Any) -> Any:
        if not isinstance(args, Hashable):
            return func(*args)
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        print("Calculating new result")
        cache_dict[args] = func(*args)
        return cache_dict[args]
    cache_dict = {}
    return inner
