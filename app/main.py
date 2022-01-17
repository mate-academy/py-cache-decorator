import functools


def cache(func):

    memory = {}

    @functools.wraps(func)
    def wrapper(*args):
        nonlocal memory
        if args in memory and memory[args][0] == func.__name__:
            print("Getting from cache")
            return memory[args][1]

        else:
            memory[args] = func.__name__, func(*args)
            print("Calculating new result")
            return func(*args)

    return wrapper
    pass
