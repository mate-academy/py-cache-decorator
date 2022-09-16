def cache(func):
    save_value = {}

    def inner(*args, **kwargs):
        if args in save_value:
            print("Getting from cache")
        else:
            save_value[args] = func(*args, **kwargs)
            print("Calculating new result")
        return save_value[args]
    return inner
