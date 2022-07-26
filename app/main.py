def cache(func):
    name_of_the_function = {}

    def inner(*args, **kwargs):
        nonlocal name_of_the_function
        if args in name_of_the_function:
            print("Getting from cache")
            return name_of_the_function[args]
        else:
            print("Calculating new result")
            if isinstance(args, str):
                name_of_the_function[args] = args
            else:
                name_of_the_function[args] = func(*args)
                return name_of_the_function[args]

    return inner
