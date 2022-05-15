def cache(func):

    lis = []

    def inner(*args):

        if args not in lis:
            lis.append(args)
            print("Calculating new result")
        else:
            print("Getting from cache")

    return inner

