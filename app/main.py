from typing import Callable


def cache(func: Callable) -> Callable:
    temp_cache = {}
    def decorate(*args, **kwargs) -> None:
        key = "_".join(map(str, args))
        if key not in temp_cache:
            temp_cache[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return temp_cache[key]
    return decorate
