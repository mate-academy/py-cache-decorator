def cache(func):
    dict_with_args = {}

    def wrapper(*args):
        nonlocal dict_with_args
        if args in dict_with_args:
            print("Getting from cache")
            return dict_with_args[args]

        dict_with_args.update({args: func(*args)})
        print("Calculating new result")
        return func

    return wrapper
