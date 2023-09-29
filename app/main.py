from typing import Callable


def cache(func: Callable) -> Callable:
    cached_arguments = []
    cached_results = []

    def wrapper(*args, **kwargs) -> int:
        if args in cached_arguments or kwargs in cached_arguments:
            print("Getting from cache")
            return cached_results[cached_arguments.index(args)]
        else:
            cached_arguments.append(args)
            cached_results.append(func(*args, **kwargs))
            print("Calculating new result")
            return cached_results[-1]

    return wrapper
