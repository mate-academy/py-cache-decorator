from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        cached_args = args + tuple(kwargs.items())
        if cached_args not in wrapper.cached_calls:
            wrapper.cached_calls[cached_args] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return wrapper.cached_calls[cached_args]
    wrapper.cached_calls = dict()

    return wrapper
