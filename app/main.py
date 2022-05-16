def cache(func):

    long_time_list = []

    def inner(*args, **kwargs):

        list_args = [*args]
        if list_args in long_time_list:
            print("Getting from cache")
        else:
            print("Calculating new result")
        long_time_list.append([*args])
        return func(*args, **kwargs)
    return inner
