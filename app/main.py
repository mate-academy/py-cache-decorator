def cache(func):
    results = {}

    def wrapper(*args):
        if args not in results:
            print("Calculating new result")
            results[args] = func(*args)
        else:
            print("Getting from cache")
        return results[args]
    return wrapper
