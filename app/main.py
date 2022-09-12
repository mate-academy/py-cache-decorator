def cache(func):
    cache_list = {}

    def wrapper(*args, **kwargs):
        if args in cache_list:
            print("Getting from cache")
            return cache_list[args]
        else:
            print("Calculating new result")
            new_value = func(*args)
            cache_list[args] = new_value
            return new_value
    return wrapper
