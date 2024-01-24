from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args: tuple) -> Any:
        func_was_calculating = args not in cache_dict.keys()
        if func_was_calculating:
            cache_dict[args] = func(*args)

        print(["Getting from cache",
               "Calculating new result"][func_was_calculating])

        return cache_dict[args]
    return wrapper
