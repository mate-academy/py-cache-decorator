from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def inner(*args) -> int:
        if args not in cached_results:
            print("Calculating new result")
            cached_results[args] = func(*args)
        else:
            print("Getting from cache")

        return cached_results.get(args)

    return inner
