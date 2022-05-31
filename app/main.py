from functools import wraps

dict_cache = {}


def cache(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if f"{func.__name__} {args}" in dict_cache:
            print("Getting from cache")
            return dict_cache[f"{func.__name__} {args}"]
        else:
            dict_cache.update({f"{func.__name__} {args}": func(*args, **kwargs)})
            print("Calculating new result")
            return func(*args, **kwargs)

    return wrapper
