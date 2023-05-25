from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_data = {}

    def wrapper(*args) -> Any:
        message = "Getting from cache"
        if args not in stored_data:
            message = "Calculating new result"
            stored_data[args] = func(*args)
        print(message)
        return stored_data[args]
    return wrapper
