from typing import Callable


def cache(func: Callable) -> Callable:
    cache_item = {}

    def long_time(*args) -> str:

        if args not in cache_item.keys():
            cache_item[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_item[args]
    return long_time
