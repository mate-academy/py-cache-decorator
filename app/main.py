from typing import Callable, Any


def cache(func: Callable) -> Any:
    cache_dict = {}

    def wrapper(*args) -> Any:
        if hash(args) in cache_dict:
            print("Getting from cache")
            return cache_dict[hash(args)]
        else:
            func_res = func(*args)
            cache_dict[hash(args)] = func_res
            print("Calculating new result")
            return func_res

    return wrapper
