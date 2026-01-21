from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args, **kwargs) -> Any:
        key = str(args + tuple(sorted(kwargs.items())))
        if key in results:
            print("Getting from cache")
            return results[key]
        else:
            print("Calculating new result")
            results[key] = func(*args, **kwargs)
            return results[key]

    return wrapper
