def cache(func):
    cache_dict = {}

    def wrapper(*args):
        if args not in cache_dict:
            cache_dict.update({args: func(*args)})
            print("Calculating new result")
            return cache_dict[args]
        else:
            print("Getting from cache")
            return cache_dict[args]

    return wrapper
