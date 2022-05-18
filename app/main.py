def cache(func):

    long_time_list = {}

    def inner(*args, **kwargs):

        if tuple(args) in long_time_list:
            print("Getting from cache")
        else:
            print("Calculating new result")
            long_time_list[tuple(args)] = func(*args, **kwargs)
        return long_time_list[tuple(args)]
    return inner
