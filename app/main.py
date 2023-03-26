def cache(func):
    cashe = {}

    def inner(*args, **kwargs):
        if args in cashe:
            print("Getting from cache")
            return cashe[args]
        else:
            print("Calculating new result")
            cashe[args] = func(*args)
            return cashe[args]
    return inner
