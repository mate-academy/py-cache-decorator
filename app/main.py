def cache(func: callable) -> callable:
    my_dict = {}

    def wrapper(*args) -> callable:

        if args in my_dict:
            print("Getting from cache")
            return my_dict[args]
        my_dict[args] = func(*args)
        print("Calculating new result")

        return my_dict[args]
    return wrapper
