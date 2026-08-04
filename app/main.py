from typing import Callable


def cache(func: Callable) -> Callable:
    cache1 = {}

    def dec(*args, **kwargs) -> Callable:
        # nonlocal cache1
        key = (args, tuple(kwargs))
        if key in cache1:
            print("Getting from cache")
            return cache1[key]
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
            cache1[key] = res
            return res
    return dec
