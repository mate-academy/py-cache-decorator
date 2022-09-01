def cache(func):

    dict_for_cache = {}

    def inner(*args):
        if args in dict_for_cache:
            print("Getting from cache")
            return dict_for_cache[args]
        dict_for_cache[args] = func(*args)
        print("Calculating new result")
        return dict_for_cache[args]

    return inner
