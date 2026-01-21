from typing import Callable


def cache(func: Callable) -> Callable:
    # Dictionary to store cached results for each function
    func_cache = {}

    def wrapper(*args, **kwargs) -> any:
        # Create a key from the function name and arguments
        # Since we're only dealing with immutable arguments,
        # we can use them as dict keys
        key = (func.__name__, args, frozenset(kwargs.items()))

        if key in func_cache:
            print("Getting from cache")
            return func_cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            func_cache[key] = result
            return result

    return wrapper
