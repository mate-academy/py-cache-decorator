def cache(func: callable) -> any:
    # This dictionary is local to the function being decorated
    stored_results = {}

    def wrapper(*args: any) -> any:
        # Using the arguments tuple as a key in our dictionary
        if args in stored_results:
            print("Getting from cache")
            return stored_results[args]

        print("Calculating new result")
        result = func(*args)
        stored_results[args] = result
        return result

    # Manually copying basic metadata so the function
    # doesn't just look like "wrapper"
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__

    return wrapper
