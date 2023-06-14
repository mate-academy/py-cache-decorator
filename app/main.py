from typing import Callable, Any


def cache(func: Callable) -> None:
    results = {}

    def wrapper(*args, **kwargs) -> Any:
        key = args + tuple(kwargs.items())
        if key in results:
            print("Getting from cache")
            return results[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            results[key] = result
            return result

    return wrapper
