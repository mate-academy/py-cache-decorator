from typing import Callable, Union


def cache(func: Callable) -> Callable:
    cached_data = {}

    def wrapper(*args) -> Union[int, list]:
        key = args
        if key in cached_data:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached_data[key] = func(*args)
        return cached_data[key]
    return wrapper
