from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        kwargs_tuple = tuple(sorted(kwargs.items()))
        cache_key = (args, kwargs_tuple)

        if cache_key in cache_dict:
            print("Getting from cache")
            return cache_dict[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[cache_key] = result
        return result

    return wrapper
