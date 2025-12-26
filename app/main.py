from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_data = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in cache_data:
            print("Getting from cache")
            return cache_data[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_data[cache_key] = result
        return result

    return wrapper
