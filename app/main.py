from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    launch_cache = dict()

    @wraps(func)
    def wrapper(*args) -> Any:
        if args in launch_cache:
            print("Getting from cache")
            return launch_cache[args]
        print("Calculating new result")
        result = func(*args)
        launch_cache[args] = result
        return result
    return wrapper
