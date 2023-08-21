def cache(func):
    cache_dict = {}
    def inner(*args, **kwargs):
        if (args, tuple(kwargs.items())) in cache_dict:
            print("Getting from cache")
            return cache_dict[(args, tuple(kwargs.items()))]
        else:
            result = func(*args, **kwargs)
            print("Calculating new result")
            cache_dict[(args, tuple(kwargs.items()))] = result
            return result
    return inner
