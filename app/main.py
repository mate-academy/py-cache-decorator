from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args, **kwargs) -> Any:
        # Create a cache key from arguments
        # Convert kwargs to a sorted tuple of items for consistent hashing
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in cache_storage:
            print("Getting from cache")
            return cache_storage[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[cache_key] = result
            return result

    return wrapper
