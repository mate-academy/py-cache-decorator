from functools import wraps


def cache(func):
    """New decoration function with cache"""
    cache_data = {}

    @wraps(func)
    def wrapper(*args):
        cache_key = (id(func), *args,)
        if cache_key not in cache_data:
            res = func(*args)
            cache_data[cache_key] = res
            print("Calculating new result")
        else:
            res = cache_data[cache_key]
            print("Getting from cache")
        return res

    return wrapper
