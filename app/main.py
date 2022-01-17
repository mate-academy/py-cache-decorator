def cache(func):
    caches = {}

    def inner(*args):
        if args in caches.keys():
            print("Getting from cache")
            return caches[args]
        else:
            print("Calculating new result")
            result = func(*args)
            caches[tuple(args)] = result
            return result
    return inner
