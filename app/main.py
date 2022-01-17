def cache(func):
    cache_dict = {}

    def inner(*args, **kwargs):
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        else:
            cache_dict[args] = func(*args)
            print("Calculating new result")
            return func(*args, **kwargs)

    return inner
