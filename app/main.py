from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_store = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))

        result = cache_store.get(key)

        if result is not None:
            print("Getting from cache")
        else:
            result = func(*args, **kwargs)
            cache_store[key] = result
            print("Calculating new result")
        return result

    return wrapper
