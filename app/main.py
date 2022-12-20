from typing import Any


def cache(func: callable) -> callable:
    results = {}

    def wrapper(*args: Any) -> Any:
        if args not in results:
            value = func(*args)
            results[args] = value
            print("Calculating new result")
            return value

        elif args in results:
            print("Getting from cache")
            return results[args]
    return wrapper
