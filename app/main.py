from typing import Callable, Any, MutableSequence


def cache(func: Callable) -> Callable:
    cache_memory = {}

    def wrapper(*args: not MutableSequence) -> Any:

        if args in cache_memory:
            print("Getting from cache")
            result = cache_memory[args]
        else:
            result = func(*args)
            cache_memory[args] = result
            print("Calculating new result")

        return result

    return wrapper
