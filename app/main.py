from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_archive = {}

    def wrapper(*args: tuple) -> Any:

        if args in cache_archive.keys():
            print("Getting from cache")
            result = cache_archive[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_archive[args] = result

        return result

    return wrapper
