def cache(func):
    cache_dict = {}

    def inner(*args):
        if hash(args) in cache_dict:
            print("Getting from cache")
            return cache_dict[hash(args)]
        else:
            print("Calculating new result")
            some_data = func(*args)
            cache_dict[hash(args)] = some_data
            return some_data
    return inner
