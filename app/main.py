from typing import Callable


def cache(func: Callable) -> Callable:
    cached_data: dict = {}

    def wrapper(*args, **kwargs) -> int:
        if args in cached_data:
            print("Getting from cache")
            return cached_data[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_data[args] = result
            return result

    return wrapper
