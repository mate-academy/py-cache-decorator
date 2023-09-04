from functools import wraps


def cache(func: callable) -> callable:
    cache_store = {}

    @wraps(func)
    def wrapper(*args) -> any:
        if args not in cache_store.keys():
            print("Calculating new result")
            cache_store[*args] = func(*args)
        else:
            print("Getting from cache")
        return cache_store[*args]
    return wrapper
