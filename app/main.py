from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    """
    A decorator that caches the results of function calls
    with immutable arguments. It prints a message indicating
    whether the result is from the cache or newly calculated.
    """
    # This dictionary will be unique for each function decorated with @cache,
    # as it's created when the decorator is applied.
    _cache = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        The wrapper function that handles caching logic.
        """
        # We create a single, hashable key from all arguments.
        # We sort kwargs.items() to ensure that calls like func(a=1, b=2)
        # and func(b=2, a=1) are treated as the same call.
        key = (args, tuple(sorted(kwargs.items())))

        if key in _cache:
            print("Getting from cache")
            return _cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            _cache[key] = result
            return result

    return wrapper
