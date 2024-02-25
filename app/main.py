from typing import Callable, Any, Tuple


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args: Tuple[Any], **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))

        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result

    return wrapper
