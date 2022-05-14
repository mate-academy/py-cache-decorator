def cache(func):
    cached_results = {}

    def inner(*args):
        if args in cached_results:
            print("Getting from cache")
            return cached_results[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cached_results[args] = result
            return result
    return inner
