def cache(func):
    cache_dictionary = {}

    def inner(*args):
        if args in cache_dictionary:
            print("Getting from cache")
            return cache_dictionary[args]

        else:
            print('Calculating new result')
            cache_dictionary[args] = (res := func(*args))
            return res
    return inner
