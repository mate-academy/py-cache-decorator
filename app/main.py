from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args: tuple, **kwargs: dict) -> int:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]

        # Checking if function parameters immutable,
        # because they are cannot be keys

        if kwargs:
            return func(*args, **kwargs)
        for arg in args:
            if not isinstance(arg, (int, float, bool, str, tuple)):
                return func(*args, **kwargs)

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[args] = result
        return result

    return wrapper
