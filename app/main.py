from typing import Callable, Any


def cache(func: Callable) -> Callable:
    history_def = {}

    def wrapper(*args: Any) -> Callable:
        if args not in history_def:
            print("Calculating new result")
            history_def[args] = func(*args)
            return history_def[args]

        print("Getting from cache")
        return history_def[args]

    return wrapper
