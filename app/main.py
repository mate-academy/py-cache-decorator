def cache(func):
    cache_result = {}

    def wrapper(*args, **kwargs):
        if args in cache_result:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_result[args] = func(*args, **kwargs)
        return cache_result[args]
    return wrapper
