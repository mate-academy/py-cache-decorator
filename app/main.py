
def cache(func):

    d = {}

    def wrapper(*args):
        if args not in d:
            d[args] = func(*args)
            print("Calculating new result")
            return d[args]
        elif args in d:
            print("Getting from cache")
            return d[args]

    return wrapper


@cache
def subtraction(a, b):
    return a - b
