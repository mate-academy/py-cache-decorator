def cache(func: callable) -> callable:
    previous_function_calls = {}
    if func.__name__ not in previous_function_calls.keys():
        previous_function_calls[func.__name__] = {}

    def wrapper(*args) -> int:
        if args not in previous_function_calls[func.__name__]:
            print("Calculating new result")
            previous_function_calls[func.__name__][args] = func(*args)
            return previous_function_calls[func.__name__][args]
        else:
            print("Getting from cache")
            return previous_function_calls[func.__name__][args]
    return wrapper
