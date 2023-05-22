from functools import wraps

def cache(func):
    results = {}

    @wraps(func)
    def wrapper(*args):
        if args in results:
            print("Getting from cache")
            return results[args]
        else:
            print("Calculating new result")
            result = func(*args)
            results[args] = result
            return result

    return wrapper
