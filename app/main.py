from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    launch_cache = dict()

    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        key = str(args) + str(kwargs)
        if func.__name__ in launch_cache:
            if key in launch_cache[func.__name__]:
                print("Getting from cache")
                return launch_cache[func.__name__][key]
            else:
                print("Calculating new result")
                launch_cache[func.__name__][key] = func(*args, **kwargs)
                return launch_cache[func.__name__][key]
        else:
            launch_cache[func.__name__] = dict()
            print("Calculating new result")
            launch_cache[func.__name__][key] = func(*args, **kwargs)
            return launch_cache[func.__name__][key]

    return wrapper
