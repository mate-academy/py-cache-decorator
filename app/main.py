def cache(func):
    result = {}

    def inner(*args):
        if args not in result:
            result[args] = func(*args)
            print("Calculating new result")
            return func(*args)
        else:
            print("Getting from cache")
            return result[args]
    return inner
