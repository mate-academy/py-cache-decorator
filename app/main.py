from typing import Callable, Union


def cache(func: Callable) -> Callable:
    cached_data = {}

    def wrapper(*args, **kwargs) -> Union[int, list]:
        key = (args, tuple(kwargs.items()))
        if key in cached_data:
            print("Getting from cache")
            result = cached_data[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_data[key] = result
        return result
    return wrapper
