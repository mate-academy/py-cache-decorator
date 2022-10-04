import functools


def cache(func):
    @functools.wraps(func)

    cache_keys = []
    cache_result = []

    def wrapper(*args):
        cache_key = (id(func), *args,)
        if cache_key not in cache_keys:
            res = func(*args)
            cache_keys.append(cache_key)
            cache_result.append(res)
            print("Calculating new result")
        else:
            index = cache_keys.index(cache_key)
            res = cache_result[index]
            print("Getting from cache")
        return res

    return wrapper

