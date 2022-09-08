def cache(function):
    data_array = {}

    def runtime(*data):
        if data in data_array:
            print("Getting from cache")
        else:
            print("Calculating new result")
            function_result = function(*data)
            data_array[data] = function_result
        return data_array[data]

    return runtime
