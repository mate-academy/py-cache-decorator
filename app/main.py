from typing import Callable


def cache(func: Callable) -> Callable:
    cache_results = {}

    def inner(*args, **kwargs) -> Callable:
        tuple_of_numbers = (args, tuple(kwargs.items()))
        if tuple_of_numbers in cache_results:
            print("Getting from cache")
            return cache_results[tuple_of_numbers]

        print("Calculating new result")
        cache_results[tuple_of_numbers] = func(*args, **kwargs)
        return cache_results[tuple_of_numbers]

    return inner
