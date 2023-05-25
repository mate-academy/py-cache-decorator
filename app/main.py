from typing import Callable


def cache(func: Callable) -> Callable:
    stored_cashe = {}

    def wrapper(*args) -> str:
        if args in stored_cashe:
            print("Getting from cache")
            return stored_cashe[args]
        else:
            new_result = func(*args)
            stored_cashe[args] = new_result
            print("Calculating new result")
            return new_result
    return wrapper
