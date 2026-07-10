from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage: dict[tuple, Any] = {}

    def wrapper(*args, **kwargs) -> Any:
        cache_key = (args, tuple(sorted(kwargs.items())))
        if cache_key in storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            storage[cache_key] = func(*args, **kwargs)
        return storage[cache_key]

    return wrapper
