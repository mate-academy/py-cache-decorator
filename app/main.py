from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in cached_results:
            print("Getting from cache")
        else:
            cached_results[key] = func(*args, **kwargs)
            print("Calculating new result")

        return cached_results[key]

    return wrapper
