from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_store = {}

    def wrapper(*args, **kwargs) -> Any:
        args_tuple = (args, tuple((kwargs.items())))
        if args_tuple in cached_store:
            print("Getting from cache")
            return cached_store[args_tuple]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cached_store[args_tuple] = result
        return result

    return wrapper
