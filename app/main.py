from functools import wraps


def cache(func):
    results = {}

    @wraps(func)
    def wrapper(*args):
        if args in results:
            print("Getting from cache")
        else:
            results[args] = func(*args)
            print("Calculating new result")

        return results[args]
    return wrapper
