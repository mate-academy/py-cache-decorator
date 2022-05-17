def cache(func):
    caches = {}

    def inner(*args):
        if args in caches:
            print("Getting from cache")
        else:
            print("Calculating new result")
            caches[args] = func(*args)

        return caches[args]
    return inner
