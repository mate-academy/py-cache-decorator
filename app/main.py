def cache(func):
    cache_date = {}

    def wrapper(*args):
        if args in cache_date:
            print("Getting from cache")
        else:
            cache_date[args] = func(*args)
            print("Calculating new result")
        return cache_date[args]
    return wrapper
