from typing import Callable, Any


def cache(func: Callable) -> Callable:
    res_cache = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in res_cache:
            print("Getting from cache")
        else:
            res_cache[key] = func(*args, **kwargs)
            print("Calculating new result")
        return res_cache[key]
    return wrapper
