from typing import Callable


def cache(func: Callable) -> Callable:
    cached_data = {}

    def inner(*args, **kwargs) -> None:
        if args in cached_data.keys():
            print("Getting from cache")
        else:
            new_cache = func(*args)
            cached_data[args] = new_cache
            print("Calculating new result")

        return func(*args) if args not in cached_data.keys() else cached_data[args]

    return inner
