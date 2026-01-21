from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    archive_args = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if args in archive_args:
            print("Getting from cache")
        else:
            archive_args[args] = func(*args, **kwargs)
            print("Calculating new result")
        return archive_args[args]
    return wrapper
