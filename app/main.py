from typing import Callable


def cache(func: Callable) -> Callable:
    cached_result = {}

    def wripper(*args, **kwargs) -> Callable:
        a, b, c = args
        if (a, b, c) not in cached_result:
            result = func(a, b, c)
            cached_result[a, b, c] = result
            print("Calculating new result")
        else:
            print("Getting from cache")
    return wripper
