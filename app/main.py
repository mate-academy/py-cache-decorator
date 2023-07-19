from typing import Callable, Any


def cache(func: tuple) -> Callable:
    archive = {}

    def inner(*args, **kwargs) -> Any:
        if args not in archive:
            result = func(*args, **kwargs)
            archive[args] = result
            print("Calculating new result")
        else:
            print("Getting from cache")
        return archive[args]
    return inner
