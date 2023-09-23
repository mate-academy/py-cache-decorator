from typing import Callable


def cache(func: Callable) -> Callable:
    archive = {}

    def inner(*args) -> int:
        if args in archive:
            print("Getting from cache")
            return archive.get(args)
        else:
            archive[args] = func(*args)
            print("Calculating new result")
            return archive[args]
    return inner
