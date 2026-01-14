from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    def inner(*args, **kwargs) -> Any:
        key = make_hash_key(*args, **kwargs)
        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_results[key] = result
            return result

    return inner


def make_hash_key(*args, **kwargs) -> dict:
    return (args, tuple(sorted(kwargs.items())))
