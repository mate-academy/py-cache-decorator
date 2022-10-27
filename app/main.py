def cache(func):
    cache_dict = {}

    def wrapper(*args):
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        else:
            print("Calculating new result")
            res = func(*args)
            cache_dict[args] = res
            return res
    return wrapper

