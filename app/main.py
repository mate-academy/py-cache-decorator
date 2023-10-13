from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))

        if key in results.keys():
            print("Getting from cache")
            return results[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        results[key] = result

        return results[key]

    return wrapper
