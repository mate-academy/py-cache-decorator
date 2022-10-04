def cache(func):
    cache_storage = {}

    def inner(*args):
        if (*args,) in cache_storage:
            print("Getting from cache")
        else:
            cache_storage[(*args,)] = func(*args)
            print("Calculating new result")

        return cache_storage[(*args,)]

    return inner
