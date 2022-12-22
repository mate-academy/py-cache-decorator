from typing import Any


def cache(func: callable) -> callable:
    results = {}

    def wrapper(*args, **kwargs: Any) -> Any:
        if args not in results:
            print("Calculating new result")
            results[args] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return results[args]
    return wrapper
