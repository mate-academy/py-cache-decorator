def cache(func):
    cache_results = {}

    def inner(*args):
        if args in cache_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_results[args] = func(*args)
        return cache_results[args]

    return inner
