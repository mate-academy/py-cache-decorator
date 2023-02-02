from typing import Callable, Any


def cache(func: Callable) -> Callable:
    database = {}

    def inner(*args) -> Any:
        if args in database:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args)
            database[args] = result
        return database[args]

    return inner
