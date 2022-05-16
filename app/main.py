def cache(func):
    # I made the comments below for myself,
    # it's easier for me to understand the topic

    data_dictionary = {}  # Create data for store results

    def wrapper(*args):  # Create wrapper function
        # Check input data -> compare with existing
        if args in data_dictionary.keys():
            print("Getting from cache")  # If they are -> print
            return data_dictionary[args]  # And return them
        else:  # If there aren't input data do this
            print("Calculating new result")  # If they aren't -> print
            result = func(*args)
            data_dictionary[args] = result  # Input data pass to func
            return result  # return func with input data

    return wrapper  # Return wrapper function
