from typing import Callable, Any


def cache(func: Callable) -> Callable:
    inner_cache = {}

    def inner(*args, **kwargs) -> Any:
        dict_key = (args, frozenset(kwargs.items()))
        if dict_key in inner_cache:
            print("Getting from cache")
            return inner_cache[dict_key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        inner_cache[dict_key] = result
        return result

    return inner
