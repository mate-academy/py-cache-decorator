from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = str(args) + str(kwargs)
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]

        result = func(*args, **kwargs)
        cache_dict[key] = result
        print("Calculating new result")
        return result

    return wrapper
