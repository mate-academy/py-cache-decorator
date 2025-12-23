from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def get_key_by_args(*args, **kwargs) -> tuple:
        return args, tuple(sorted(kwargs.items()))

    def inner(*args, **kwargs) -> Any:
        cache_key = get_key_by_args(*args, **kwargs)

        if cache_key not in cache_dict:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[cache_key] = result
        else:
            print("Getting from cache")

        return cache_dict[cache_key]

    return inner
