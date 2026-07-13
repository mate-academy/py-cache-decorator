from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_info = {}

    def inner(*args, **kwargs) -> Any:
        if args in cached_info:
            print("Getting from cache")
        else:
            result_of_function = func(*args, **kwargs)
            cached_info[args] = result_of_function
            print("Calculating new result")
        return cached_info[args]
    return inner
