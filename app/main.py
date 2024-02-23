from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args, **kwargs) -> Any:
        args_tuple = tuple(args)
        if args_tuple in cached_results:
            print("Getting from cache")
            return cached_results[args_tuple]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_results[args_tuple] = result
            return result

    return wrapper
