def cache(func):
    cache_dict = {}

    def inner(*args):

        if args in cache_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_dict[args] = func(*args)
        return cache_dict[args]

    return inner
