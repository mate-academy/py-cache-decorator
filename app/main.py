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
        cached_results[args] = func(*args)
        print("Calculating new result")
        return cached_results[args]

    return wrapper
