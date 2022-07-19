def cache(func):
    temp_dict = {}

    def inner(*args):

        if args in temp_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            temp_dict[args] = func(*args)
        return temp_dict[args]
    return inner
