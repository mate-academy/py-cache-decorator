from typing import Callable, Any


def cache(func: Callable) -> Callable:
    temp_cache = {}

    def decorate(*args, **kwargs) -> Any:

        key = (args, tuple(sorted(kwargs.items())))

        if key not in temp_cache:
            temp_cache[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return temp_cache[key]
    return decorate
