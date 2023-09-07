from functools import wraps


def cache(func: callable) -> callable:
    inner_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> any:
        if args in inner_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            inner_cache[args] = func(*args)
        return inner_cache[args]
    return wrapper
