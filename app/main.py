
def cache(func):

    array = {}

    def wrapper(*args):
        if args not in array:
            array[args] = func(*args)
            print("Calculating new result")

        elif args in array:
            print("Getting from cache")

        return array[args]

    return wrapper
