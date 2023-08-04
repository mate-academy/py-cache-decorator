def cache(func: callable) -> callable:
    stored_results = {}

    def wrapper(*args) -> callable:
        if args in stored_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            stored_results[args] = func(*args)

        return stored_results[args]

    return wrapper
