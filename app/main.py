def cache(func):

    cache_list = {}

    def wrapper(*args):
        if args in cache_list.keys():
            print("Getting from cache")
            return cache_list[args]
        else:
            print("Calculating new result")
            cache_list[args] = func(*args)
            return func(*args)
    return wrapper
