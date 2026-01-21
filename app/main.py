from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    dict_result = {}

    @wraps(func)
    def inner(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in dict_result:
            print("Getting from cache")
        else:
            print("Calculating new result")
            dict_result[key] = func(*args, **kwargs)
        return dict_result[key]

    return inner
