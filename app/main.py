from typing import Callable, Any


def cache(func: Callable) -> Callable:
    dict_cache: dict[tuple, Any] = {}

    def wrapper(*args, **kwargs) -> Any:
        values_kwargs = tuple(kwargs.values())
        values = (*args, *values_kwargs)
        if values in dict_cache:
            print("Getting from cache")
            return dict_cache[values]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            dict_cache[values] = result
            return result

    return wrapper
