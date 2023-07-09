from functools import wraps


def cache(func: callable) -> callable:
    caches = {}

    @wraps(func)
    def wrapper(*args: tuple) -> None:
        if args in caches:
            print("Getting from cache")
            return caches[args]

        result = func(*args)
        caches[args] = result
        print("Calculating new result")
        return result
    return wrapper
