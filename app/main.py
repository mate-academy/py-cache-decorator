def cache(func):
    count = {}

    def wrapper(*args):
        nonlocal count

        if args in count.keys():
            print("Getting from cache")
        else:
            count[args] = func(*args)
            print("Calculating new result")

        return count[args]

    return wrapper
