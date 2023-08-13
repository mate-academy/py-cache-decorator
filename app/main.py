from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_data = dict()

    def wrapper(*args: Any) -> int | str:
        for argument in args:
            if isinstance(argument, (list, set, dict)):
                return "Arguments must be immutable type."
        if args not in cache_data:
            cache_data[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_data[args]
    return wrapper
