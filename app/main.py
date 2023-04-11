from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = str(args) + str(kwargs)

        if key not in cache_dict:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[key] = result
        print("Getting from cache")
        return cache_dict[key]

    return wrapper
