def cache(func):
    dict_cache = {}

    def inner(*args):
        if args not in dict_cache:
            dict_cache[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return dict_cache[args]

    return inner
