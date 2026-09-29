from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cache_results = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache_results:
            print("Getting from cache")
            return cache_results[key]

        print("Calculating new result")
        result = func(*args, **kwargs)

        cache_results[key] = result
        return result

    return wrapper
