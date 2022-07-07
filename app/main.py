def cache(func):
    cache_base = {}

    def inner(*args):
        nonlocal cache_base
        if args in cache_base:
            print("Getting from cache")
        else:
            cache_base[args] = func(*args)
            print("Calculating new result")
        return cache_base[args]

    return inner
