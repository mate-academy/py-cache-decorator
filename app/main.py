from typing import Callable


def cache(func: Callable) -> Callable:
    res = {}
    def caching(*args, **kwargs):
        if args not in res:
                res[args] = func(*args, **kwargs)
                print("Calculating new result")
        elif args in res:
            print("Getting from cache")
        return res[args]
    return caching