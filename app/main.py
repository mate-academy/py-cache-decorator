def cache(func: callable) -> callable:
    stored_results = {}

    def inner(*args) -> callable:
        if args not in stored_results:
            stored_results[args] = func(*args)
            print("Calculating new result")
            return stored_results[args]

        print("Getting from cache")
        return stored_results[args]

    return inner
