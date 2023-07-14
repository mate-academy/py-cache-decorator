from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_data_storage = {}

    def wrapper(*args, **kwargs) -> Any:
        if cached_data_storage.get(args) is None:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_data_storage[args] = result
        else:
            print("Getting from cache")
        return cached_data_storage[args]
    return wrapper
