def cache(func):
    res_cache = {}

    def inner(*args):
        if args in res_cache:
            print("Getting from cache")
        else:
            res_cache[args] = func(*args)
            print("Calculating new result")
        return res_cache[args]

    return inner
    pass
