def cache(func):
    count = {}

    def wrapper(*args):

        if args in count:
            print("Getting from cache")
        else:
            count[args] = func(*args)
            print("Calculating new result")

        return count[args]

    return wrapper
