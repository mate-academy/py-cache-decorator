from typing import Callable, Any


def cache(func: Callable) -> Any:
    cache_data = {}

    def memory(*args: tuple) -> Any:
        if args in cache_data:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_data[args] = func(*args)

        return cache_data[args]

    return memory
