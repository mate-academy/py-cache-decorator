from typing import Callable, Any


def cache(func: Callable) -> Callable:
    caching_results = {}

    def wrapper(*args) -> Any:
        cach_key = args
        if cach_key in caching_results.keys():
            print("Getting from cache")
            return caching_results[args]
        else:
            print("Calculating new result")
            func_result = func(*args)
            caching_results[args] = func_result
            return func_result

    return wrapper
