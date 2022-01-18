def cache(func):
    cache_dictionary = {}

    def inner(*args):
        if args in cache_dictionary:
            print("Getting from cache")
            return cache_dictionary[args]
        else:
            print("Calculating new result")
            var = func(*args)
            cache_dictionary[args] = var
            return var

    return inner
