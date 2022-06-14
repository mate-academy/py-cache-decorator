def cache(func):
    cache_data = {}

    def wrapper(*args):
        if args not in cache_data:
            print("Calculating new result")
            new_value = func(*args)
            cache_data[args] = new_value
            return new_value

        print("Getting from cache")
        return cache_data[args]

    return wrapper
