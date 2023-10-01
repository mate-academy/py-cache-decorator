from typing import Callable


def cache(func: Callable) -> Callable:
    cache_results = {}

    def wrapper(*args, **kwargs) -> None:
        arg_key = (args, frozenset(kwargs.items()))
        if arg_key in cache_results:
            print("Getting from cache")
            return cache_results[arg_key]
        else:
            result = func(*args, **kwargs)
            cache_results[arg_key] = result
            print("Calculating new result")
            return result

    return wrapper
