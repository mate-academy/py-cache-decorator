from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache1 = {}

    def dec(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs))
        if key in cache1:
            print("Getting from cache")
            return cache1[key]
        print("Calculating new result")
        cache1[key] = func(*args, **kwargs)
        return cache1[key]
    return dec
