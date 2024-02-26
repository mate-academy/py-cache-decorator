from typing import Callable


def cache(func: Callable) -> Callable:
    results = dict()

    def wrapper_cache(*args, **kwargs) -> int:
        if args in results:
            print("Getting from cache")

            return results[args]

        results[args] = func(*args, **kwargs)
        print("Calculating new result")

        return results[args]

    return wrapper_cache
