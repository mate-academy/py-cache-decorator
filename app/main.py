def cache(func):
    cache_dict = {}

    def inner(*args, **kwargs):
        if args not in cache_dict:
            result = func(*args, **kwargs)
            cache_dict[args] = result
            print("Calculating new result")
            return result
        print("Getting from cache")
        return cache_dict[args]
    return inner
