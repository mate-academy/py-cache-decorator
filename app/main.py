from typing import Callable, Any


def cache(func: Callable) -> Callable:
    inner_cache = {}

    def inner(*args, **kwargs) -> Any:
        if args in inner_cache.keys():
            print("Getting from cache")
            return inner_cache[args + tuple(kwargs.values())]
        print("Calculating new result")
        result = func(*args, **kwargs)
        inner_cache[args + tuple(kwargs.values())] = result
        return result
    return inner


