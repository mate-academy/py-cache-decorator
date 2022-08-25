def cache(func):
    cache_dict = {}

    def wrapper1(*args):
        if args not in cache_dict:
            cache_dict[args] = func(args)
            print("Calculating new result")
            return cache_dict[args]
        else:
            print("Getting from cache")
            return cache_dict[args]
    return wrapper1
