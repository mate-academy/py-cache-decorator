from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_cache = {}

    def wrapper(*args, **kwargs) -> Any:
        key = args + tuple(kwargs.items())

        if key in result_cache:
            print("Getting from cache")
            return result_cache[key]

        print("Calculating new result")
        result_cache[key] = func(*args, **kwargs)
        return result_cache[key]

    return wrapper
