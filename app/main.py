from functools import wraps
from typing import Callable, Any

_cached_funcs = {}


def cache(func: Callable) -> Callable:
    """
        A decorator that caches function results
        based on function and input arguments.

        If the function is called with the same arguments as a previous call,
        the cached result is returned instead of recomputing the result.
        Otherwise, the function executes and stores the result in the cache.

        :param func: The function to be decorated.
        :type func: Callable
        :return: The wrapped function with caching capability.
        :rtype: Callable
    """

    @wraps(func)
    def wrapper(*args) -> Any:
        was_arguments_used = False
        result = None

        # Check if the function has been cached before
        if func in _cached_funcs:
            # Iterate through cached results for this function
            for element in _cached_funcs[func]:
                # Compare stored arguments with the current arguments
                if element["arguments"] == [*args]:
                    # Retrieve the cached result and mark that it was used
                    result = element["result"]
                    was_arguments_used = True

        # If the function result was found in the cache,
        # return the cached value
        if was_arguments_used:
            print("Getting from cache")
            # Return cached result
            return result
        else:
            # Otherwise, compute the result and store it in the cache
            print("Calculating new result")
            result = func(*args)
            # Add the new result to the cache,
            # associating it with the function and arguments
            _cached_funcs.setdefault(func, []).append(
                {
                    "arguments": [*args],
                    "result": result
                })
            # Return the newly computed result
            return result

    return wrapper
