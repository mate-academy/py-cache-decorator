def cache(func):
    c_dict = {}

    def inner(*args):
        if args in c_dict:
            print("Getting from cache")
            return c_dict[args]
        else:
            print("Calculating new result")
            s = func(*args)
            c_dict[args] = s
            return s

    return inner
