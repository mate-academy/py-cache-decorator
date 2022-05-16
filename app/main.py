def cache(func):
    results = {}

    def inner(*args):
        if args in results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            results[args] = func(*args)

        return results[args]

    return inner
