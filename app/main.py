def cache(func):
    stored_results = {}

    def inner(*args):
        if args not in stored_results:
            stored_results[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return stored_results[args]

    return inner
