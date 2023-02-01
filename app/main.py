from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args, **kwargs) -> tuple:
        arguments = (*args, *kwargs.values())

        if arguments not in cache_dict:
            result = func(*args, **kwargs)
            cache_dict[arguments] = result
            print("Calculating new result")
            return result

        print("Getting from cache")
        return cache_dict[arguments]

    return inner
