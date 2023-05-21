def cache(func):
    data = {}

    def inner(*args):
        if args in data:
            print("Getting from cache")
        else:
            print("Calculating new result")
            data[args] = func(*args)
        return data[args]
    return inner
