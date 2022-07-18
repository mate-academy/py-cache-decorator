def cache(func):
    temp_dict = {}
    def inner(*args):
        if args in temp_dict:
            print(f"Getting from cache")
        else:
            print(f"Calculating new result")
            temp_dict[args] = func(*args)
        return temp_dict[args]
    return inner
