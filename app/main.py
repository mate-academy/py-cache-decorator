from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dictionary = {}

    def inner(*args, **kwargs) -> None:
        key = (args, tuple(kwargs.items()))

        if key in cache_dictionary.keys():
            print("Getting from cache")
            result = cache_dictionary[key]
            return result

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dictionary[key] = result

        return result

    return inner
