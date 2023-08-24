from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    caching_result = []

    @wraps(func)
    def wrapper(*args) -> Any:
        for item in caching_result:
            if args in item:
                print("Getting from cache")
                return item[args]

        print("Calculating new result")
        result = func(*args)
        caching_result.append({
            args: result
        })

        return result

    return wrapper
