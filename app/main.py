def cache(func):
    new_dict = {}

    def inner(*args, **kwargs):
        if args not in new_dict:
            new_dict[args] = func(*args)
            print("Calculating new result")

        else:
            print("Getting from cache")
        return new_dict.get(args)
    return inner
