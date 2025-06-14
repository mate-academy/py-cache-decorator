import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_list = []
    functools.wraps(func)

    def wrapper(*args, **kwargs) -> str:
        for caches in cache_list:
            if caches[0] == args and caches[1] == tuple(kwargs.items()):
                print("Getting from cache")
                return caches[2]
        result = func(*args, **kwargs)
        cache_list.append((args, tuple(kwargs.items()), result))
        print("Calculating new result")
        return result

    return wrapper
