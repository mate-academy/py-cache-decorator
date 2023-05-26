def cache(func):
    dict_cache = {}

    def wrapper(*args, **kwargs):
        key = (*args, *kwargs.values())
        if key not in dict_cache:
            dict_cache[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return dict_cache.get(key)

    return wrapper
