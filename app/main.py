def cache(func):
    cache_dict = {}

    def inner(*args, **kwargs):
        if args in cache_dict:
            print("Getting from cache")
        else:
            cache_dict[args] = func(*args, **kwargs)
            print("Calculating new result")
        return cache_dict[args]

    return inner
