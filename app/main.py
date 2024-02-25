from typing import Callable


def cache(func: Callable) -> Callable:
    results = dict()

    def wrapper_cache(*args, **kwargs) -> int:
        if args in results:
            print("Getting from cache")

            return results[args]

        result = func(*args, **kwargs)
        results[args] = result
        print("Calculating new result")

        return result

    return wrapper_cache
