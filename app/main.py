from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_data = {}

    def inner(*args) -> Any:
        if func not in cache_data:
            cache_data[func] = {}

        if args in cache_data[func]:
            print("Getting from cache")
            return cache_data[func][args]
        else:
            print("Calculating new result")
            result_of_func = func(*args)
            cache_data[func][args] = result_of_func
            return result_of_func

    return inner
