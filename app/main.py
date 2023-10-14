from typing import Callable


def cache(func: Callable) -> Callable:
    results_cache = {}

    def wrapper(*args, **kwargs) -> None:
        args_tuple = args + tuple(kwargs.items())
        if args_tuple in results_cache:
            print("Getting from cache")
            return results_cache[args_tuple]
        else:
            result = func(*args, **kwargs)
            results_cache[args_tuple] = result
            print("Calculating new result")
            return result

    return wrapper
