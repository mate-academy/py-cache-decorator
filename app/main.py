def cache(func):

    long_time_list = {}

    def inner(*args, **kwargs):

        if args in long_time_list:
            print("Getting from cache")
        else:
            print("Calculating new result")
            long_time_list[args] = func(*args, **kwargs)
        return long_time_list[args]
    return inner
