from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_cashe = {}

    def wrapper(*args) -> Any:
        if args in stored_cashe:
            print("Getting from cache")
        else:
            stored_cashe[args] = func(*args)
            print("Calculating new result")
        return stored_cashe[args]
    return wrapper
