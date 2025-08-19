from typing import Any, Callable


def cache(func: Callable) -> Callable:
    results_cache = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in results_cache:
            print("Getting from cache")
            return results_cache[key]
        else:
            print("Calculating new result",)
            results_cache[key] = func(*args, **kwargs)
            return results_cache[key]
    return wrapper
