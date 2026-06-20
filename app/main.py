from typing import Callable


def cache(func: Callable) -> Callable:
    cache_data = {}
    f_name = func.__name__
    if f_name not in cache_data:
        cache_data[f_name] = {}
    cur_cache = cache_data[f_name]

    def inner(*args) -> Callable:
        if args in cur_cache:
            print("Getting from cache")
            return cur_cache[args]
        result = func(*args)
        cur_cache[args] = result
        print("Calculating new result")
        return result

    return inner
