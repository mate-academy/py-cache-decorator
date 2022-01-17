def cache(func):
    arr = []

    def inner(*args, **kwargs):
        if args in arr:
            print("Getting from cache")
            return func(*args, **kwargs)
        else:
            arr.append(args)
            print("Calculating new result")
            return func(*args, **kwargs)

    return inner
