def cache(func):
    unique = set()

    def inner(*args):
        if args not in unique:
            unique.add(args)
            print("Calculating new result")
            return func(*args)
        else:
            print("Getting from cache")
            return unique

    return inner
