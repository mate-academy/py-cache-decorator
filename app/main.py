from typing import Callable


def cache(func: Callable) -> Callable:
    cached_data = {}

    def searcher(*args) -> Callable:
        if args in cached_data:
            print("Getting from cache")
            return cached_data[args]
        result = func(*args)
        cached_data[args] = result
        print("Calculating new result")
        return result

    return searcher
