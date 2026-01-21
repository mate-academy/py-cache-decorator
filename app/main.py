from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:

        nonlocal results

        if func in results:
            if args + tuple(sorted(kwargs.items())) in results[func]:
                print("Getting from cache")
                return results[func][args + tuple(sorted(kwargs.items()))]
        else:
            results[func] = {}

        print("Calculating new result")
        result = func(*args, **kwargs)
        results[func][args + tuple(sorted(kwargs.items()))] = result

        return result
    return wrapper
