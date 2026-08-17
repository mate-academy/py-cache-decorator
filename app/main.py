from typing import Any, Callable


def cache(func: Callable) -> Callable:
    results_cache = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in results_cache:
            print("Getting from cache")
            return results_cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            results_cache[key] = result
            return result
    return wrapper
