from typing import Callable


def cache(func: Callable) -> Callable:

    cache_results = {}

    def inner(*args) -> Callable:

        data_key = args, func.__name__

        if data_key in cache_results.keys():

            print("Getting from cache")
            return cache_results[data_key]

        print("Calculating new result")

        result = func(*args)
        cache_results[data_key] = result

        return result

    return inner
