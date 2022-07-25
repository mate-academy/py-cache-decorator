def cache(func):
    name_of_the_function = {}

    def inner(*args, **kwargs):
        if name_of_the_function is False or func.__name__ \
                not in name_of_the_function:
            print("Calculating new result")
            name_of_the_function[func.__name__] = {}
            if isinstance(args, str):
                name_of_the_function[func.__name__][args] = args
            else:
                result = func(*args)
                name_of_the_function[func.__name__][args] = result
                return result

        elif args in name_of_the_function[func.__name__]:
            print("Getting from cache")
            return name_of_the_function[func.__name__][args]

        else:
            print("Calculating new result")
            if isinstance(args, str):
                name_of_the_function[func.__name__][args] = args
            else:
                result = func(*args)
                name_of_the_function[func.__name__][args] = result
                return result
    return inner
