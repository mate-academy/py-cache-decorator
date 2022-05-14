def cache(func):
    functions = dict()
    arguments = set()

    def inner(*args):
        if func.__name__ in functions and args in arguments:
            print("Getting from cache")
            return functions[func.__name__]
        else:
            print("Calculating new result")
            functions[func.__name__] = func(*args)
            arguments.add(args)
            return func(*args)
    return inner
