def cache(func):
    results = {}

    def wrapper(*args, **kwargs):
        if args in results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            results[args] = func(*args)

        return results[args]

    return wrapper
