from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_data = {}

    def inner(*args, **kwargs) -> Any:
        cache_key = (tuple(args), tuple(kwargs))

        if cache_key in cache_data:
            print("Getting from cache")

            return cache_data[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_data[cache_key] = result

        return result

    return inner
