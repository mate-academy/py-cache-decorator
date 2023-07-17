def cache(func):
    cache_dict = {}

    def wrapper(*args, **kwargs):
        key = (tuple(args), tuple(kwargs.items()))

        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result

    return wrapper
