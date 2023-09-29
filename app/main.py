from typing import Callable


def cache(func: Callable) -> Callable:
    cached = {}

    def inner(*args, **kwargs) -> None:
        if args in cached.keys():
            print("Getting from cache")
        else:
            new_cache = func(*args)
            cached[args] = new_cache
            print("Calculating new result")

        return func(*args) if args not in cached.keys() else cached[args]

    return inner
