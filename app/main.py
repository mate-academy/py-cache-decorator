from typing import Callable, Any


def cache(func: Callable) -> Callable:
    # This dictionary is unique for every function decorated with @cache
    results = {}

    def wrapper(*args, **kwargs) -> Any:
        # 'args' is already a tuple, which is immutable and hashable.
        # We can use it directly as a dictionary key.
        if args in results:
            print("Getting from cache")
            return results[args]

        print("Calculating new result")
        result = func(*args, **kwargs)

        # Store the result using the arguments as the key
        results[args] = result
        return result

    return wrapper
