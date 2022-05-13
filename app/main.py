def cache(func):
    res = {}

    def inner(*args, **kwargs):
        if args in res:
            print("Getting from cache")
            return res[args]
        else:
            print("Calculating new result")
            res[args] = func(*args)
            return res[args]
    return inner
