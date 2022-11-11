def cache(func):
    cache_storage = {}

    def inner(*args, **kwargs):
        if args not in cache_storage:
            cache_storage[args] = func(*args)
            print("Calculating new result")
        elif args in cache_storage:
            print("Getting from cache")
        return cache_storage[args]
    return inner
