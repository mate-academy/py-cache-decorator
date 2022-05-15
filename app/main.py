def cache(func):
    cached_values_list = []

    def inner(*args, **kwargs):
        nonlocal cached_values_list

        sublist = [*args]

        if sublist in cached_values_list:
            print("Getting from cache")
        else:
            print("Calculating new result")

        cached_values_list += [[*args]]

        return func(*args, **kwargs)

    return inner
