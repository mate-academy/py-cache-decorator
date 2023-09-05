from typing import Callable

cache_values = {}


def cache(func: Callable) -> Callable:
    def inner(*args) -> None:
        if (args, func) not in cache_values.keys():
            cache_values[(args, func)] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_values[(args, func)]
    return inner
