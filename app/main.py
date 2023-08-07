from typing import Callable, Any


def cache(func: Callable) -> Callable:

    result_cache = {}

    def wrapper(*args: Any) -> Any:
        if args in result_cache:
            print("Getting from cache")
            return result_cache[args]

        result_cache[args] = func(*args)
        print("Calculating new result")
        return result_cache[args]
    return wrapper
