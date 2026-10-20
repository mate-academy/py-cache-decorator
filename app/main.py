from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cache_data = {}

    def wrapper(*args: Any) -> Any:
        if args in cache_data:
            print("Getting from cache")
            return cache_data[args]

        print("Calculating new result")
        result = func(*args)
        cache_data[args] = result
        return result

    return wrapper
