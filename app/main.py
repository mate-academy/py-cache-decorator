from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args, **kwargs) -> None:
        cache_key = (args, tuple(sorted(kwargs.items())))
        if cache_key in result:
            print("Getting from cache")
            return result[cache_key]
        else:
            print("Calculating new result")
            new_result = func(*args, **kwargs)
            result[cache_key] = new_result
            return new_result
    return wrapper
