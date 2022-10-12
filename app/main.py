def cache(func):
    cache_collector = {}

    def wrapper(*args):
        if args not in cache_collector:
            print("Calculating new result")
            cache_collector[args] = func(*args)
        else:
            print("Getting from cache")
        return cache_collector[args]
    return wrapper
