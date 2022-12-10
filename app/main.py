def cache(func):
    results = {}
    if func.__name__ not in results.keys():
        results[func.__name__] = {}

    def wrapper(*args):
        if args not in results[func.__name__]:
            print("Calculating new result")
            results[func.__name__][args] = func(*args)
            return results[func.__name__][args]
        else:
            print("Getting from cache")
            return results[func.__name__][args]
    return wrapper
