from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    launch_cache = dict()

    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        key = str(args) + str(kwargs)
        if func in launch_cache:
            if key in launch_cache[func]:
                print("Getting from cache")
                return launch_cache[func][key]
            else:
                print("Calculating new result")
                launch_cache[func][key] = func(*args, **kwargs)
                return launch_cache[func][key]
        else:
            launch_cache[func] = dict()
            print("Calculating new result")
            launch_cache[func][key] = func(*args, **kwargs)
            return launch_cache[func][key]

    return wrapper
