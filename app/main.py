def cache(func):
    cache_dict = {}
    def wrapper(*args):
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        else:
            result_new = func(*args)
            cache_dict[args] = result_new
            print("Calculating new result")
            return result_new

    return wrapper
