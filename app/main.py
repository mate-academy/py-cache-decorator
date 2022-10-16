def cache(func):

    cache_results = {}

    def wrapper(*args):
        if args in cache_results:
            print("Getting from cache")
        else:
            cache_results[args] = func(*args)
            print("Calculating new result")
        return cache_results[args]
    return wrapper
