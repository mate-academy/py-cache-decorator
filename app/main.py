from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_result = {}

    def inner(*args, **kwargs) -> Any:
        if args in cached_result:
            print("Getting from cache")
        else:
            cached_result[args] = func(*args, **kwargs)
            print("Calculating new result")
        return cached_result[args]
    return inner
