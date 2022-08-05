import functools


def cache(func):
    global_cache = dict({})

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # if (func.__name__, args) in global_cache:
        if args in global_cache:
            print("Getting from cache")
            return global_cache[args]
        else:
            print("Calculating new result")
        res = func(*args)
        global_cache[args] = res
        return res
    return wrapper
