caches = []


def cache(func):
    def inner(*args, **kwargs):
        global caches
        if args in caches:
            print("Getting from cache")
        else:
            caches.append(args)
            print("Calculating new result")
    return inner
