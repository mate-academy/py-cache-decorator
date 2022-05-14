def cache(func):
    arg_dict = {}

    def inner(*args):
        if args not in arg_dict.keys():
            result = func(*args)
            arg_dict[args] = result
            print("Calculating new result")

            return result
        else:
            print("Getting from cache")

            return arg_dict[args]

    return inner
