from functools import wraps


def cache(func):
    f_name = func.__name__
    dict_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if f"{args}" in dict_cache:
            print("Getting from cache")
            return dict_cache[f"{args}"]
        else:
            dict_cache.update({f"{args}": func(*args)})
            print("Calculating new result")
            return dict_cache[f"{args}"]

    return wrapper
