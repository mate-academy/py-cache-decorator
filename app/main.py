from typing import Callable
import functools

def cache(func: Callable) -> Callable:
    cache_list = []
    functools.wraps(func)
    def wrapper(*args, **kwargs) -> str:
        output = func(*args, **kwargs)
        for cache in cache_list:
            if cache[0] == args and cache[1] == kwargs and cache[2] == output:
                return "Getting from cache"
            else:
                cache_list.append((args, kwargs, output))
                return "Calculating new result"
    return wrapper