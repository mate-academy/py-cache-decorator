from typing import Callable


def cache(func: Callable) -> any:
    cache_dictionary = {}

    def inner(*args, **kwargs) -> str:
        cache_item = func.__name__ + "".join(str(args)) + "".join(str(kwargs))
        if cache_item in cache_dictionary:
            print("Getting from cache")
            return cache_dictionary[cache_item]
        print("Calculating new result")
        cache_dictionary[cache_item] = func(*args, **kwargs)
        return cache_dictionary[cache_item]
    return inner
