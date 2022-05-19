def cache(func):
    cached_values = []

    def inner(*args):

        lst = [*args]

        if lst in cached_values:
            print("Getting from cache")
        else:
            print("Calculating new result")

        cached_values.append([*args])

        return func(*args)

    return inner
