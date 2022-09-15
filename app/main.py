def cache(func):
    cache = {}

    def inner(*args):

        if args in cache:  # check previous results
            print("Getting from cache")
        else:
            # if result not in cache,
            # add result in cache and return cache
            cache[args] = func(*args)
            print("Calculating new result")

        return cache[args]
    return inner
