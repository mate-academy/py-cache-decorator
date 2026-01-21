from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache = {}

    def innit(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache:
            print("Getting from cache")
            return cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache[key] = result
            return result

    return innit
