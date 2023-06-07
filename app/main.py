
def cache(func):
    cache_dict = {}

    def wrapper(*args, **kwargs):
        if args not in cache_dict:
            print("Calculating new result")
            cache_dict[args] = func(*args, **kwargs)
            return cache_dict[args]
        else:
            print("Getting from cache")
            return cache_dict[args]
    return wrapper
