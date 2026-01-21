from functools import wraps
from typing import Callable, Optional, Dict


def cache(func: Callable) -> Callable:
    """
    Decorator that caches function results based on their arguments.

    This decorator stores the results of function calls in a dictionary using
    the function's arguments as keys. When the decorated function is called
    with the same arguments again, it returns the cached result instead of
    re-executing the function.

    Features:
    - Each decorated function maintains its own independent cache
    - Supports both positional and keyword arguments
    - Works only with immutable argument types (int, str, tuple, etc.)
    - Prints "Calculating new result" when computing new values
    - Prints "Getting from cache" when returning cached values

    Args:
        func (Callable): The function to be decorated. Should accept only
                        immutable arguments for proper cache key generation.

    Returns:
        Callable: A wrapped version of the function with caching functionality.
    """
    func_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Optional[Dict]:
        """
        Wrapper function that implements the caching logic.

        Args:
            *args: Positional arguments passed to the decorated function
            **kwargs: Keyword arguments passed to the decorated function

        Returns:
            The result of the function call (either cached or newly computed)
        """
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in func_cache:
            print("Getting from cache")
            return func_cache[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)

        func_cache[cache_key] = result

        return result

    return wrapper
