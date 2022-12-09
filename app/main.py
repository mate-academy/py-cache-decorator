from typing import Callable, Any


def cache(func: Callable) -> Callable:
    history = {}

    def wrapper(*args, **kwargs) -> Any:
        if args not in history:
            history[args] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return history[args]
    return wrapper
