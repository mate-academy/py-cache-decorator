from typing import Callable


def cache(func: Callable) -> Callable:

    cache_results = {}

    def inner(*args) -> Callable:

        data_key = args

        if data_key in cache_results.keys():

            print("Getting from cache")
            return cache_results[data_key]

        print("Calculating new result")

        cache_results[data_key] = func(*args)

        return cache_results[data_key]

    return inner
