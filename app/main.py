from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args):
        if args in storage:
            print("Getting from cache")
            return storage[args]

        print("Calculating new result")
        result = func(*args)
        storage[args] = result
        return result

    return wrapper


    pass
