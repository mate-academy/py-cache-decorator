def cache(func):
    results = {}

    def inner(*args):
        if args in results is not None:
            print("Getting from cache")
            return results[args]

        print("Calculating new result")
        results[args] = func(*args)
        return results[args]

    return inner
