from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    result_dict = {}

    @functools.wraps(func)
    def inner(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))

        if key not in result_dict:
            print("Calculating new result")
            result_dict[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return result_dict[key]

    return inner
