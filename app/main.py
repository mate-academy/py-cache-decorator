from typing import Callable


def cache(func: Callable) -> Callable:
    memory_dict = {}

    def wrapper(*args, **kwargs) -> Callable:
        cache_key = (args, tuple(kwargs.items()))
        if cache_key not in memory_dict:
            print("Calculating new result")
            memory_dict[cache_key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return memory_dict[cache_key]
    return wrapper
