from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args, **kwargs) -> Any:
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in results:
            print("Getting from cache")
            return results[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        results[cache_key] = result
        return result
    return wrapper
