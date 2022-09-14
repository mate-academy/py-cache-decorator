def cache(func):
    cache_storage_base = dict()

    def wrapper(*args):
        if args in cache_storage_base:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_storage_base[args] = func(*args)

        return cache_storage_base[args]

    return wrapper
