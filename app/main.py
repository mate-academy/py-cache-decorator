def cache(func):
    new_cache = {}

    def inner(*args):
        if args in new_cache:
            print("Getting from cache")
        else:
            new_cache[args] = func(*args)
            print("Calculating new result")
        return new_cache[args]
    return inner
