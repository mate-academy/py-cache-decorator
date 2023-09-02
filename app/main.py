def cache(func):
    data = {}

    def inner(*args):
        if args in data:
            print("Getting from cache")
            return data[args]
        else:
            data[args] = func(*args)
            print("Calculating new result")
            return data[args]
    return inner
