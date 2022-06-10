def cache(func):
    cache_dictionary = {}

    def inner(*args):
        if args in cache_dictionary:
            print("Getting from cache")
        else:
            cache_dictionary[args] = func(*args)
            print("Calculating new result")
        return cache_dictionary[args]
    return inner
