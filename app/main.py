from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_results = {}

    def wrapper(*args: (int, float, bool, str, bytes, tuple)) -> Any:
        key = f"{func.__name__}: {args}"
        if key in cache_results.keys():
            print("Getting from cache")
            return cache_results[key]
        else:
            func_result = func(*args)
            cache_results[key] = func_result
            print("Calculating new result")
            return func_result
    return wrapper
