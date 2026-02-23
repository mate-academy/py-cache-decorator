from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_func_results = {}

    def wrapper(*args) -> Any:
        if args not in cached_func_results:
            print("Calculating new result")
            result = func(*args)
            cached_func_results[args] = result
        else:
            print("Getting from cache")
            result = cached_func_results.get(args)
        return result

    return wrapper
