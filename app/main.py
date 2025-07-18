from typing import Callable


def cache(func: Callable) -> Callable:
    # Write your code here
    pass
    result_cache: dict[tuple, object] = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in result_cache:
            print("Getting from cache")
            return result_cache[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        result_cache[key] = result
        return result

    return wrapper