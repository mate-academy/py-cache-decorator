from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_cache = {}

    def wrapper(*args: Any) -> Any:
        if args in result_cache:
            print("Getting from cache")
            return result_cache[args]
        print("Calculating new result")
        result = func(*args)
        result_cache[args] = result
        return result
    return wrapper
