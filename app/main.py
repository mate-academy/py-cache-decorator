def cache(func):
    functions = dict()

    def inner(*args):
        if args in functions:
            print("Getting from cache")
            return functions[args]
        else:
            print("Calculating new result")
            functions[args] = func(*args)
            return func(*args)
    return inner
