from typing import Callable


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = args + tuple(sorted(kwargs.items()))
        if func in cache:
            if key in cache[func]:
                print("Getting from cache")
                return cache[func][key]
            else:
                print("Calculating new result")
                result = func(*args, **kwargs)
                cache[func][key] = result
                return result
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache[func] = {key : result}
            return result

    return wrapper
