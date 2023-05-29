from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_cache = {}

    def wrapper(*args: Any) -> Any:
        if args not in result_cache:
            print("Calculating new result_cache")
            result_cache[args] = func(*args)
        else:
            print("Getting from cache")

        return result_cache.get(args)

    return wrapper
