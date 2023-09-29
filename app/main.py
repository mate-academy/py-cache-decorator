from typing import Callable


def cache(func: Callable) -> Callable:

    cached_results_storage = {}

    def inner(*args, **kvargs) -> int:
        if args in cached_results_storage:
            print("Getting from cache")
            return cached_results_storage.get(args)
        else:
            print("Calculating new result")
            result = func(*args, **kvargs)
            cached_results_storage[args] = result
            return result
    return inner
