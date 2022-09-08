def cache(func):
    cache_dict = {}

    def wrapper(*args):
        if args in cache_dict:
            print("Getting from cache")
        else:
            cache_dict[args] = func(*args)
            print("Calculating new result")
        return cache_dict[args]
    return wrapper
