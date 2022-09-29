def cache(func):
    old_cache = {}

    def wrapper_cache(*args):
        if args in old_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            old_cache[args] = func(*args)
        return old_cache[args]
    return wrapper_cache

