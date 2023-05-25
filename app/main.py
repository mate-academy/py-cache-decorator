from typing import Callable


def cache(func: Callable) -> Callable:
    stored_cashe = {}

    def wrapper(*args) -> int:
        if args in stored_cashe:
            print("Getting from cache")
            return stored_cashe[args]

        stored_cashe[args] = func(*args)
        print("Calculating new result")
        return stored_cashe[args]
    return wrapper
