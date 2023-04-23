from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args) -> Any:
        if not all(isinstance(
                arg,
                (int, float, str, bool, tuple))
                for arg in args):
            return func(*args)
        if args in cached_results:
            print("Getting from cache")
            return cached_results[args]
        result = func(*args)
        cached_results[args] = result
        print("Calculating new result")
        return result

    return wrapper
