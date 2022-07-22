def cache(func):
    name_of_the_function = {}
    if func.__name__ not in name_of_the_function:
        name_of_the_function[func.__name__] = {}

    def inner(*args, **kwargs):
        if len(name_of_the_function[func.__name__]) == 0:
            print("Calculating new result")
            try:
                result = func(*args)
                name_of_the_function[func.__name__][args] = result
                return result
            except TypeError:
                name_of_the_function[func.__name__][args] = args

        elif args in name_of_the_function[func.__name__]:
            print("Getting from cache")
            return name_of_the_function[func.__name__][args]

        else:
            print("Calculating new result")
            try:
                name_of_the_function[func.__name__][args] = func(*args)
                return func(*args)
            except TypeError:
                name_of_the_function[func.__name__][args] = args
    return inner
