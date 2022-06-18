def cache(func):
    cache = {}

    def inner(*args):
        if args in cache:
            print("Getting from cache")
        else:
            cache[args] = func(*args)
            print("Calculating new result")
        return cache[args]
    return inner
