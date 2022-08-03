import functools


def cache(func):
    global_cache = dict({})

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if (func.__name__, args) in global_cache:
            print("Getting from cache")
            return global_cache[(func.__name__, args)]
        else:
            print("Calculating new result")
            # global_cache.append((func.__name__, args))
        if func.__name__ == "long_time_func":
            a, b, c = args
            res = func(a, b, c)
            global_cache[(func.__name__, args)] = res
            return res
        a, b = args
        res = func(a, b)
        global_cache[(func.__name__, args)] = res
        return res
    return wrapper
