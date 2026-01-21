from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    """
    This decorator caches the result of a function
    :param func: original function
    :return: wrapped function
    """
    cache_data = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        """
        This wrapper will cache the result of a function
        :param args: args
        :param kwargs: kwargs
        :return: Calculation data or Cached data
        """
        key = args + tuple(sorted(kwargs.items()))

        if key not in cache_data:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_data[key] = result
            return result
        else:
            print("Getting from cache")
            return cache_data[key]

    return wrapper
