from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dictionary = {}

    def wrapper(*args, **kwargs) -> Any:
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key not in cache_dictionary:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dictionary[cache_key] = result
        else:
            print("Getting from cache")
            result = cache_dictionary[cache_key]

        return result
    return wrapper
