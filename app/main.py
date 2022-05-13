def cache(func):
    dict_with_args = {}

    def wrapper(*args):
        if args in dict_with_args:
            print("Getting from cache")
            return dict_with_args[args]

        dict_with_args.update({args: func(*args)})
        print("Calculating new result")
        return dict_with_args[args]

    return wrapper
