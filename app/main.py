from typing import Callable


def cache(func: tuple) -> str:
    archive = {}

    def inner(*args, **kwargs) -> Callable:
        if args not in archive:
            result = func(*args, **kwargs)
            archive[args] = result
            print("Calculating new result")
        else:
            print("Getting from cache")
        return archive[args]
    return inner
