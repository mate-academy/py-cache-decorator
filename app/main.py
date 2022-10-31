def cache(func):
    dict_of_args = {}

    def wrapper(*args):
        if args not in dict_of_args:
            print("Calculating new result")
            dict_of_args[args] = func(*args)
        else:
            print("Getting from cache")

        return dict_of_args[args]

    return wrapper
