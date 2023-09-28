from typing import Callable, Any


def cache(func: Callable) -> Callable:
    caching_results = {}

    def wrapper(*args) -> Any:
        key = args
        if key in caching_results:
            print("Getting from cache")
            return caching_results[args]
        else:
            print("Calculating new result")
            func_result = func(*args)
            caching_results[args] = func_result
            return func_result

    return wrapper
