from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))

        if key not in results:
            value_result = func(*args, **kwargs)
            results[key] = value_result
            print("Calculating new result")

        else:
            print("Getting from cache")

        return results[key]

    return wrapper
