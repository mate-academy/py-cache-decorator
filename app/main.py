def cache(func):
    cache_storage = {}

    def wrapper(*args):
        if args not in cache_storage:
            print("Calculating new result")
            cache_storage[args] = func(*args)
        else:
            print("Getting from cache")
        return cache_storage[args]
    return wrapper
