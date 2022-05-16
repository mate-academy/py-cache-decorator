def cache(func):
    cache_dict = {}

    def inner(*args):
        mutable = False
        if type(args) in [list, dict, set]:
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
                return func(*args)
    return inner
