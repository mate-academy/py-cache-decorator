def cache(func):
    saved_funcs = {}

    def inner(*args):
        if not saved_funcs.get(args, False) is not False:
            res = func(*args)
            saved_funcs[args] = res
            print("Calculating new result")
            return res
        else:
            print("Getting from cache")
            return saved_funcs[args]

    return inner
