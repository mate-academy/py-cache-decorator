def cache(func):
    dict1 = {}

    def inner(*args):
        if args in dict1:
            print("Getting from cache")
            return dict1[args]
        else:
            res = func(*args)
            dict1.update({args: res})
            print("Calculating new result")
            return res

    return inner
