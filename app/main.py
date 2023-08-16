from typing import Callable


def cache(func: Callable) -> Callable:
    caching_place = {}

    def wrapper(*args, **kwargs) -> None:
        arguments = args + tuple(sorted(kwargs.items()))
        if arguments in caching_place:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            caching_place[arguments] = result
        return caching_place[arguments]
    return wrapper
