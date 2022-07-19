def cache(func):
    count = 0
    dict_of_args = {}

    def wrapper(*args):
        nonlocal count
        nonlocal dict_of_args
        count += 1
        if count == 1 or args not in dict_of_args:
            print("Calculating new result")
            dict_of_args[args] = func(*args)
        else:
            print("Getting from cache")

        return dict_of_args[args]

    return wrapper
