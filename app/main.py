from functools import wraps


def cache(func):
    f_name = func.__name__
    dict_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if f"{f_name} {args}" in dict_cache:
            print("Getting from cache")
            return dict_cache[f"{f_name} {args}"]
        else:
            dict_cache.update({f"{f_name} {args}": func(*args, **kwargs)})
            print("Calculating new result")
            return func(*args, **kwargs)

    return wrapper
