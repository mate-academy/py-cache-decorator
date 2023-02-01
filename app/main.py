from typing import Callable


def cache(func: Callable) -> Callable:
    database = {}

    def inner(*args) -> Callable:
        if args in database:
            print("Getting from cache")
            return database[args]
        print("Calculating new result")
        result = func(*args)
        database[args] = result
        return result

    return inner
