from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args) -> Any:
        key = ", ".join(map(str, [*args]))
        cache_value = cache_dict.get(key)
        if cache_value is not None:
            print("Getting from cache")
            return cache_value
        print("Calculating new result")
        cache_dict[key] = func(*args)
        return cache_dict[key]
    return wrapper
