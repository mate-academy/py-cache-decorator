def cache(func):

    long_time_list = {}

    def inner(*args, **kwargs):

        list_args = [*args]
        if str(list_args) in long_time_list:
            print("Getting from cache")
            return long_time_list[str(list_args)]
        else:
            print("Calculating new result")
            long_time_list[str(list_args)] = func(*args, **kwargs)
            return func(*args, **kwargs)
    return inner
