def cache(func):
    cache_results = {}

    def inner(*args):
        for result in cache_results.keys():
            if args == result:
                print("Getting from cache")
                return cache_results[result]
        cache_results[args] = func(*args)
        print("Calculating new result")
        return cache_results[args]
    return inner
