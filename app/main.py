def cache(func):
    cache_dict = {}

    def inner(*args):
        mutable = False
        for argument in args:
            if type(argument) in [list, dict, set]:
                mutable = True
        if mutable:
            return func(*args)
        else:
            if args in cache_dict.keys():
                print("Getting from cache")
                return cache_dict[args]
            else:
                cache_dict[args] = func(*args)
                print("Calculating new result")
                return cache_dict[args]
    return inner
