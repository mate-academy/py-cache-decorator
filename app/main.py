from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        sorted_kwargs = tuple(sorted(kwargs.items(), key=lambda item: item[0]))
        cache_key = (args, sorted_kwargs)
        if cache_key in cache_storage:
            result = cache_storage[cache_key]
            print("Getting from cache")
        else:
            result = func(*args, **kwargs)
            cache_storage[cache_key] = result
            print("Calculating new result")
        return result
    return wrapper
