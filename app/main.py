def cache(func):
    cache_dict = {}

    def wrapper(*args, **kwargs):
        key = args
        if key not in cache_dict.keys():
            cache_dict[key] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_dict[key]

    return wrapper
    pass
