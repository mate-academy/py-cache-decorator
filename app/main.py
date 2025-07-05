from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*arg) -> Any:
        if arg in cache_dict:
            print("Getting from cache")
            return cache_dict.get(arg)
        result = func(*arg)
        print("Calculating new result")
        cache_dict[arg] = result
        return result
    return wrapper
