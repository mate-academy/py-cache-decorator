from typing import Callable


def cache(func: Callable) -> Callable:
    results_cache = {}

    def wrapper(*args, **kwargs) -> Callable:
        args_key = tuple(args)
        kwargs_key = tuple(kwargs.items())

        if (args_key, kwargs_key) in results_cache:
            print("Getting from cache")
            return results_cache[(args_key, kwargs_key)]

        result = func(*args, **kwargs)
        print("Calculating new result")
        results_cache[(args_key, kwargs_key)] = result
        return result

    return wrapper
