def cache(func):
    dic = {}

    def inner(*args):
        nonlocal dic
        if args in dic:
            print("Getting from cache")
        else:
            dic[args] = func(*args)
            print("Calculating new result")
        return dic[args]
    return inner
