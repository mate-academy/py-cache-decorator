from typing import Any, Callable


def cache(func: Callable) -> Callable:
    def wrapper(*args) -> Any:
        if args in wrapper.cache:
            print("Getting from cache")
            return wrapper.cache[args]
        else:
            print("Calculating new result")
            result = func(*args)
            wrapper.cache[args] = result
            return result

    wrapper.cache = {}
    return wrapper
