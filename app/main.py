def cache(func):

    cache_list_ = {}

    def wrapper(*args):
        if args in cache_list_.keys():
            print("Getting from cache")
            return cache_list_[args]
        else:
            print("Calculating new result")
            cache_list_[args] = func(*args)
            return func(*args)
    return wrapper
