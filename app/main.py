from typing import Callable, Any
cache_archive = {}


def cache(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if f"{func} {args} {kwargs}" not in cache_archive.keys():
            print("Calculating new result")
            res = func(*args, **kwargs)
            cache_archive[f"{func} {args} {kwargs}"] = res
            return res
        else:
            print("Getting from cache")
            return cache_archive[f"{func} {args} {kwargs}"]

    return wrapper
