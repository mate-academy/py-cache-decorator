from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[f"{args} - {kwargs}"]
        print("Calculating new result")
        res = func(*args, **kwargs)
        cache_dict[f"{args} - {kwargs}"] = res
        return res

    return wrapper
