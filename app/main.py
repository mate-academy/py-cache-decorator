def cache(func):

    my_memory = {}

    def wrapper(*args):

        if args in my_memory:

            print("Getting from cache")
            return my_memory[args]

        else:

            my_memory[args] = func(*args)
            print("Calculating new result")

            return func(*args)

    return wrapper
