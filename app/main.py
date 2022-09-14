def cache(func):
    cache_of_results = {}

    def wrapper(*args):
        if args in cache_of_results:
            print("Getting from cache")
            return cache_of_results[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_of_results.update({args: result})
            return result
    return wrapper
