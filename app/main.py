def cache(func):
    cache_base = {}

    def inner(*args):
        if args in cache_base:
            print("Getting from cache")
        else:
            cache_base[args] = func(*args)
            print("Calculating new result")
        return cache_base[args]

    return inner
