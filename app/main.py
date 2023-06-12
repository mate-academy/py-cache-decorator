from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}

    def inner(*args) -> Any:
        if result := results.get(args):
            print("Getting from cache")
            return result

        print("Calculating new result")
        results[args] = func(*args)
        return results.get(args)

    return inner
