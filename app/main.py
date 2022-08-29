def cache(func):

    dict_for_cache = {}

    def inner(*args):
        key_name_dict = args
        if key_name_dict in dict_for_cache:
            print("Getting from cache")
            return dict_for_cache[key_name_dict]
        new_result = func(*args)
        dict_for_cache[key_name_dict] = new_result
        print("Calculating new result")
        return new_result

    return inner
