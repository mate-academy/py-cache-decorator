from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args) -> None:
        for cache_key in cache_dict.keys():
            if cache_key == args:
                print("Getting from cache")
                return cache_dict.get(cache_key)

        results = func(*args)
        cache_dict[args] = results
        print("Calculating new result")

        return results

    return wrapper
