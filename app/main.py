def cache(func):
    cache_dict = {}

    def inner(*args):
        if hash(tuple(args)) in cache_dict:
            print("Getting from cache")
            return cache_dict[hash(tuple(args))]
        else:
            print("Calculating new result")
            some_data = func(*args)
            cache_dict[hash(tuple(args))] = some_data
            return some_data
    return inner
