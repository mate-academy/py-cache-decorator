from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args) -> None:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict.get(args)

        results = func(*args)
        cache_dict[args] = results
        print("Calculating new result")

        return results

    return wrapper
