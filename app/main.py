from typing import Callable, Any


def cache(func: Callable) -> Callable:
    archive_functions = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (func, *args)
        if key in archive_functions:
            print("Getting from cache")
        else:
            archive_functions[key] = func(*args, **kwargs)
            print("Calculating new result")
        return archive_functions[key]
    return wrapper
