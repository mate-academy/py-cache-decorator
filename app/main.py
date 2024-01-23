from typing import Callable, Any


def cache(func: Callable) -> Callable:
    dict_cache = {}

    def wrapper(*args, **kwargs) -> Any:
        item = (args, frozenset(kwargs.items()))
        if item in dict_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            dict_cache[item] = result

        return dict_cache[item]

    return wrapper
