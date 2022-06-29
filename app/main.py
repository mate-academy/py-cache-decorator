def cache(func):
    cache_dict = dict()

    def inner(*args, **kwargs):
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[args] = result
            return result

    return inner
