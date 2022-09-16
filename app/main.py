def cache(func):
    my_cache_dict = {}

    def inner(*args, **kwargs):
        if args not in my_cache_dict.keys():
            my_cache_dict[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return my_cache_dict[args]
    return inner
