def cache(func):
    results = {}

    def wrapper(*args):
        if args in results and results[args] == func(*args):
            print("Getting from cache")
            return results[args]
        else:
            print("Calculating new result")
            result = func(*args)
            results[args] = result
            return result
    return wrapper
