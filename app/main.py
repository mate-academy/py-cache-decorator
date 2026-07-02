from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args):
        if args not in cached_results:
            cached_results[args] = func(*args)
        return cached_results[args]

    return wrapper
