def cache(func: callable) -> callable:
    my_cache = dict()

    def wrapped_func(*args, **kwargs) -> callable:
        key = str(args)
        if key not in my_cache:
            print("Calculating new result")
            my_cache[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return my_cache[key]

    return wrapped_func
