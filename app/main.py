def cache(func):
    cache_result = {}

    def inner(*args):
        if args in cache_result:
            print("Getting from cache")
            return cache_result[args]
        else:
            cache_result[args] = func(*args)
            print("Calculating new result")
            return cache_result[args]

    return inner
