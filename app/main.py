from typing import Callable
import functools

def cache(func: Callable) -> Callable:
    cache_list = []
    functools.wraps(func)
    def wrapper(*args, **kwargs) -> str:
        for caches in cache_list:
            if caches[0] == args and caches[1] == kwargs:
                output = func(*args, **kwargs)
                if caches[3] == output:
                    return "Getting from caches"
        cache_list.append((args, kwargs, func(*args, **kwargs)))
        return "Calculating new result"

    return wrapper