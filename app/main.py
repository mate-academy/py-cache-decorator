def cache(func):
    dict_res = {}

    def inner(*args, **kwargs):
        if args in dict_res:
            print("Getting from cache")
        else:
            print("Calculating new result")
            dict_res[args] = func(*args)
        return dict_res[args]
    return inner
