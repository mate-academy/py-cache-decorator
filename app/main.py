def cache(func):
    data = {}

    def inner(*args):
        if args in data:
            print("Getting from cache")
            return data[args]
        else:
            print("Calculating new result")
            data[args] = func(*args)
            return data[args]
    return inner
