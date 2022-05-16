def cache(func):
    lis = []

    def inner(*args):
        if args not in lis:
            lis.append(args)
            print("Calculating new result")
            return func(*args)
        else:
            print("Getting from cache")
            return func(*args)
    return inner
