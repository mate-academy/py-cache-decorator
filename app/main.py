def cache(func):
    cache_of_args = {}

    def wrapper(*args, **kwargs):
        i = args
        if i not in cache_of_args:
            res = func(*args, **kwargs)
            cache_of_args[i] = res
            print("Calculating new result")
            return res
        if i in cache_of_args.keys():
            print("Getting from cache")
            return cache_of_args[i]
    return wrapper
