from functools import wraps


def cache(func):
    cache_result = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache_result:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_result[args] = func(*args)
        return cache_result[args]
    return wrapper
