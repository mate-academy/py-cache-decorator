from typing import Any, Callable


def cache(func: Callable) -> Callable:
    data_cache = {}

    def inner(*args: Any) -> Any:
        if args in data_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            data_cache[args] = func(*args)
        return data_cache[args]

    return inner
