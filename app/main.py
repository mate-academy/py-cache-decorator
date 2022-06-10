def cache(func):
    cache_of_args = {}

    def wrapper(*args, **kwargs):
        if args not in cache_of_args:
            res = func(*args, **kwargs)
            cache_of_args[args] = res
            print("Calculating new result")
            return res
        if args in cache_of_args.keys():
            print("Getting from cache")
        return cache_of_args[args]
    return wrapper
