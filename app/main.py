from functools import wraps
from typing import Any, Callable, Dict, Tuple


def cache(func: Callable[..., Any]) -> Callable[..., Any]: # we use "..." for specifying that the function accepts an arbitrary number of arguments of a particular type.
    cache_dict: Dict[Tuple, Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(kwargs.items()))

        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]

        print("Calculating new result")
        result = func(*args)
        cache_dict[key] = result
        return result

    return wrapper
