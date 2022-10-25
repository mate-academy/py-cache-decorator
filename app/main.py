from functools import wraps


def cache(func):
    store = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args in store.keys():
            print("Getting from cache")
            return store[args]
        maintain = func(*args, **kwargs)
        store[args] = maintain
        print("Calculating new result")
        return maintain
    return wrapper
