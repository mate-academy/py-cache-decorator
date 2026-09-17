from typing import Callable


def cache(func: Callable) -> Callable:
    results: dict[tuple, object] = {}

    def wrapper(*args: object) -> object:
        if args in results:
            print("Getting from cache")
            return results[args]

        print("Calculating new result")
        result = func(*args)
        results[args] = result

        return result

    return wrapper
