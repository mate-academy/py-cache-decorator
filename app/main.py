from typing import Callable, Any


def cache(func: Callable) -> Callable:

    cache_key = dict()

    def inner(*args, **kwargs) -> Any | None:
        key = (args, tuple(sorted(kwargs.items())))
        value = cache_key.get(key, None)
        if value is None:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_key[key] = result
            return result
        else:
            print("Getting from cache")
        return value

    return inner
