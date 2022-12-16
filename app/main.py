def cache(func: callable) -> callable:
    my_cache = dict()

    def wrapped_func(*args, **kwargs) -> callable:
        key = str(args)
        if key in my_cache:
            print("Getting from cache")
            return my_cache[key]
        my_cache[key] = func(*args, **kwargs)
        print("Calculating new result")
        return my_cache[key]

    return wrapped_func
