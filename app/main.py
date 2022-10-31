def cache(func: callable) -> callable:
    cache_storage = {}

    def inner(*args) -> callable:
        if args not in cache_storage:
            cache_storage[args] = func(*args)
            print("Calculating new result")
        elif args in cache_storage:
            print("Getting from cache")
        return cache_storage[args]
    return inner
