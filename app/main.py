def cache(func):
    cached_values_lst = []

    def inner(*args, **kwargs):

        sub_lst = [*args]

        if sub_lst in cached_values_lst:
            print("Getting from cache")
        else:
            print("Calculating new result")

        cached_values_lst.append([*args])

        return func(*args, **kwargs)

    return inner
