from functools import wraps


def cache(func):
    saved_results = {}

    @wraps(func)
    def wrapper(*args):
        if args in saved_results:
            print("Getting from cache")
            return saved_results[args]

        print("Calculating new result")
        result = func(*args)
        saved_results[args] = result
        return result

    return wrapper