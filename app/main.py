def cache(func):
    res = {}

    def wrapper(*args):
        if args in res:
            print("Getting from cache")
        else:
            res[args] = func(*args)
            print("Calculating new result")
        return res[args]

    return wrapper
