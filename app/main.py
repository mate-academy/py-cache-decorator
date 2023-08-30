from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        input_args = (args, frozenset(kwargs.items()))
        if input_args in cache_dict:
            print("Getting from cache")
            return cache_dict[input_args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[input_args] = result
            return result

    return wrapper
