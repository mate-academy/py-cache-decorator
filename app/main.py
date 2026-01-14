from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in results:
            calculation = func(*args, **kwargs)
            results[key] = calculation
            print("Calculating new result")
            return calculation
        else:
            print("Getting from cache")
            return results[key]
    return wrapper
