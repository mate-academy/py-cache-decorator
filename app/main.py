from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def inner(*args) -> int:
        if args not in cached_results:
            print("Calculating new result")
            result = func(*args)
            cached_results[args] = result
            return result

        print("Getting from cache")
        return cached_results.get(args)

    return inner
