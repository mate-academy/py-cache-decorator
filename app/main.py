from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    """
        A decorator that caches the results of function calls
        Function called with the same arguments again returns
        the cached value instead of execution
    """

    # Empty dictionary of {(args, kwargs): result}
    arguments_map = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:

        sorted_kwargs = tuple(sorted(kwargs.items()))

        cache_key = (args, sorted_kwargs)

        if cache_key in arguments_map:
            print("Getting from cache")
            return arguments_map[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)

        arguments_map[cache_key] = result

        return result
    return inner
