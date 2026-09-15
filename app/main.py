from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = []

    @wraps(func)
    def wrappers(*args, **kwargs) -> int:
        for cache_item in cache_dict:
            if (cache_item["func"] == func.__name__
                    and cache_item["args"] == args
                    and cache_item["kwargs"] == kwargs):
                print("Getting from cache")
                return cache_item["result"]
        new_result = func(*args, **kwargs)
        cache_dict.append({"func": func.__name__,
                           "args": args,
                           "kwargs": kwargs,
                           "result": new_result})
        print("Calculating new result")
        return new_result
    return wrappers
