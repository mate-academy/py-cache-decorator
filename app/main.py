import functools


def cache(func):
    cache_result = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args not in cache_result:
            cache_result[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_result.get(args)

    return wrapper
