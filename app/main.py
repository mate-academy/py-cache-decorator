from typing import Callable


def cache(func: Callable) -> Callable:
    store = {}

    def inner(*args: int, **kwargs: int) -> int:
        nonlocal store
        for key, value in store.items():
            if args == value or kwargs == value:
                print("Getting from cache")
                return key
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
            store.update({res: args})
            return res
    return inner
