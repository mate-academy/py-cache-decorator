from typing import Callable


def cache(func: Callable) -> Callable:
    cache_result = {}

    def inner(*args, **kwargs) -> Callable:
        input_data = (args, tuple(kwargs.items()))

        if input_data in cache_result:
            print("Getting from cache")
            return cache_result[input_data]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_result[input_data] = result
        return result

    return inner
