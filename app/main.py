from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args, **kwargs) -> Any:
        key = args
        if kwargs:
            key += tuple(sorted(kwargs.items()))

        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cached_results[key] = result
        return result

    return wrapper
