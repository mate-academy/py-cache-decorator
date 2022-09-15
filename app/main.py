def cache(func):
    data = {}

    def inner(*args, **kwargs):

        if args in data:
            print("Getting from cache")
        else:
            data[args] = func(*args, **kwargs)
            print("Calculating new result")

        return data[args]
    return inner
