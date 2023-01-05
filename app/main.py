from collections.abc import Hashable
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    def inner(*args: Any) -> Any:
        if not isinstance(args, Hashable):
            return func(*args)
        if args in inner.cache:
            print("Getting from cache")
            return inner.cache[args]
        print("Calculating new result")
        result = func(*args)
        inner.cache[args] = result
        return result
    inner.cache = {}
    return inner
