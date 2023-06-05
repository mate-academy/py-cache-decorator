from typing import Callable, Any


def cache(func: Callable) -> Callable:

    results = {}

    def inner(*args, **kwargs) -> Any:
        key = args

        if key in results:
            print("Getting from cache")
            return results[key]
        print("Calculating new result")
        results[key] = func(*args, **kwargs)
        return results[key]
    return inner
