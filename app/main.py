from typing import Callable, Any


IMMUTABLE_TYPES = (int, float, str, bool, tuple, bytes, type(None))


def cache(func: Callable) -> Callable:
    cache_storage: dict = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        for arg in args:
            if not isinstance(arg, IMMUTABLE_TYPES):
                return func(*args, **kwargs)
        for value in kwargs.values():
            if not isinstance(value, IMMUTABLE_TYPES):
                return func(*args, **kwargs)
        key = str((*args, *kwargs.items()))
        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[key] = result
            return result

    return wrapper
