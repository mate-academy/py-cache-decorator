def cache(func):
    # Write your code here
    dict_for_cache = {}

    def inner(*args):
        key_name_dict = args  # For search value in dictionary with name function
        if key_name_dict in dict_for_cache:
            print("Getting from cache")
            return dict_for_cache[key_name_dict]
        new_result = func(*args)
        dict_for_cache[key_name_dict] = new_result
        print("Calculating new result")
        return new_result

    return inner
