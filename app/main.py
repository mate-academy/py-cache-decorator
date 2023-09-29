from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    @functools.wraps(func)
    def wraper(*args, **kwargs) -> int:
        cache_key = func.__name__, args, tuple(kwargs.items())

        if cache_key not in wraper.execution_cache:
            func_res = func(*args, **kwargs)
            wraper.execution_cache[cache_key] = func_res

            print("Calculating new result")
            return func_res

        print("Getting from cache")
        return wraper.execution_cache[cache_key]

    wraper.execution_cache = {}

    return wraper
