def cache(func):
    result_dict = {}
    
    def wrapper(*args):
        if args in result_dict:
            print("Getting from cache")
        else:
            result_dict[args] = func(*args)
            print("Calculating new result")

        return result_dict[args]
    return wrapper
