import functools


def cache(func):
    cache_dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = f"{func}{args}"
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            cache_dict.update({key: func(*args, **kwargs)})
            print("Calculating new result")
            return cache_dict[key]
    return wrapper
