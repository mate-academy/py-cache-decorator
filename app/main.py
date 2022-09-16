import functools


def cache(func):
    cache_dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict.get(args)
        else:
            result = func(*args)
            cache_dict.update({args: result})
            print("Calculating new result")
            return result

    return wrapper
