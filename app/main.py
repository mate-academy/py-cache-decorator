from typing import Callable, Any


def cache(func: Callable) -> Callable:

    stored_results = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in stored_results:
            print("Getting from cache")
            return stored_results[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        stored_results[key] = result
        return result

    return wrapper
