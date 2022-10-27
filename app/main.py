def cache(func):
    save_values = {}

    def inner(*args, **kwargs):
        if args in save_values:
            print("Getting from cache")
        else:
            save_values[args] = func(*args, **kwargs)
            print("Calculating new result")
        return save_values[args]
    return inner
