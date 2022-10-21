from typing import Callable


def cache(func: Callable) -> Callable:
    store = {}

    def wrapper(*args, **kwargs) -> None:
        if args not in store:
            print("Calculating new result")
            immut = (float, int, tuple, str)
            if all([isinstance(arg, immut) for arg in args]):
                store[args] = func(*args, *kwargs)
                return store[args]
        else:
            print("Getting from cache")
            return store[args]
    return wrapper
