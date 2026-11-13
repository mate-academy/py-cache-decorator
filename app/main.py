from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args: Any) -> Any:
        if args not in cache_dict:
            print("Calculating new result")
            result = func(*args)
            cache_dict[args] = result
            return result

        print("Getting from cache")
        return cache_dict[args]

    return wrapper
