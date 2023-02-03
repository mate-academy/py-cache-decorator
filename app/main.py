from typing import Callable


def cache(func: Callable) -> Callable:
    cache_date = {}

    def inner(*args, **kwargs) -> any:
        if args in cache_date:
            print("Getting from cache")
            for date in cache_date:
                if date == args:
                    return cache_date[args]
        else:
            result = func(*args, **kwargs)
            cache_date[args] = result
            print("Calculating new result")
            return result

    return inner
