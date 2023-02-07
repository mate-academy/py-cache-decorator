def cache(func):
    cache_result = {}

    def wrapper(*args, **kwargs):
        if args not in cache_result:
            cache_result[args] = func(*args, *kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_result[args]

    return wrapper
