from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def inner(*args, **kwarg) -> float:
        if args not in results:
            print("Calculating new result")
            calc_res = func(*args)
            results[args] = calc_res
            return calc_res
        else:
            print("Getting from cache")
            return results[args]
    return inner
