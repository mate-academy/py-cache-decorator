from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        arguments = *args, *kwargs.values()
        if arguments not in cache_dict:
            print("Calculating new result")
            cache_dict[arguments] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cache_dict[arguments]

    return wrapper
