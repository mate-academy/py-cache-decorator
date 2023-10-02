from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_data = {}

    def argument_based_cacher(*args) -> Any:
        if func.__name__ not in cached_data.keys():
            cached_data[func.__name__] = {}
        if args in cached_data[func.__name__]:
            print("Getting from cache")
            return cached_data[func.__name__][args]
        print("Calculating new result")
        func_result = func(*args)
        cached_data[func.__name__][args] = func_result
        return func_result
    return argument_based_cacher
