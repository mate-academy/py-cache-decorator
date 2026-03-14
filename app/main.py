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

        # Convert types to make it hashable
        sorted_kwargs = tuple(sorted(kwargs.items()))

        # Create a unique fingerprint
        cache_key = (args, sorted_kwargs)

        # Check if we have calculated value
        if cache_key in arguments_map:
            # print(f"Cache found: {args} {kwargs}")
            print("Getting from cache")
            return arguments_map[cache_key]

        # Execute the original function
        # print(f"Running with arguments: {args} {kwargs}")
        print("Calculating new result")
        result = func(*args, **kwargs)

        # Save result to the map
        arguments_map[cache_key] = result

        return result
    return inner
