from typing import Any, Callable


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    cache_dict = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Convert kwargs to a sorted tuple of items so it is hashable
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            result = func(*args, **kwargs)
            cache_dict[key] = result
            print("Calculating new result")
            return result
    return wrapper
