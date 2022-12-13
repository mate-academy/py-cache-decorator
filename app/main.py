from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_archive = {}

    def wrapper(*args: tuple) -> Any:

        if args in cache_archive.keys():
            print("Getting from cache")
            res = cache_archive[args]
        else:
            print("Calculating new result")
            res = func(*args)
            cache_archive[args] = res

        return res

    return wrapper
