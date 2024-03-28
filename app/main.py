from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args, **kwargs) -> Any:
        for key in cached_results:
            if key == args:
                print("Getting from cache")
                return cached_results[key]
            if key == kwargs:
                print("Getting from cache")
                return cached_results[key]
        result = func(*args, **kwargs)
        if len(args):
            cached_results[args] = result
        else:
            cached_results[kwargs] = result
        print("Calculating new result")
        return result
    return wrapper
