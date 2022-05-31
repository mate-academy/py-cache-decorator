from functools import wraps


def cache(func):
    dict_cache = {}

    @wraps(func)
    def wrapper(*args):
        if f"{args}" in dict_cache:
            print("Getting from cache")
            return dict_cache[f"{args}"]
        else:
            dict_cache.update({f"{args}": func(*args)})
            print("Calculating new result")
            return dict_cache[f"{args}"]

    return wrapper
