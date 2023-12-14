from typing import Callable


def cache(func: Callable) -> Callable:

    cache_results = {}

    def inner(*args) -> Callable:

        if args in cache_results.keys():

            print("Getting from cache")
            return cache_results[args]

        print("Calculating new result")

        cache_results[args] = func(*args)

        return cache_results[args]

    return inner
