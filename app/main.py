def cache(func):
    results = {}

    def inner(*args):
        if args not in results:
            print("Calculating new result")
            results[args] = func(*args)
        else:
            print("Getting from cache")
        return results[args]

    return inner


