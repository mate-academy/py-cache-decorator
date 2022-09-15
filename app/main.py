def cache(function):
    cache_results = {}

    def wrapper(*args):
        if args not in cache_results:
            print("Calculating new result")
            cache_results[args] = function(*args)
        else:
            print("Getting from cache")
        return cache_results[args]

    return wrapper
