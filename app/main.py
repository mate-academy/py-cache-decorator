from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cached_value = {}

    def wpapper_func(*args) -> Any:
        if args in cached_value.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached_value[args] = func(*args)
        return cached_value[args]
    return wpapper_func
