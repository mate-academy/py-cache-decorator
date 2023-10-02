from typing import Callable
import functools


def cache(func: Callable) -> Callable:

    cached_results_storage = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> any:
        cache_key = func.__name__, args, tuple(kwargs.items())

        if cache_key not in cached_results_storage:
            func_res = func(*args, **kwargs)
            cached_results_storage[cache_key] = func_res

            print("Calculating new result")
            return func_res

        print("Getting from cache")
        return cached_results_storage[cache_key]

    return inner
