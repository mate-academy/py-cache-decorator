def cache(func):
    cache_data = {}

    def wrapper(*args):
        if args in cache_data:
            print("Getting from cache")
        else:
            cache_data[args] = func(*args)
            print("Calculating new result")
        return cache_data[args]

    return wrapper
