def cache(func):
    storage = {}
    
    def wrapper(*args):
        func_name = func.__name__
        
        if func_name in storage and args in storage[func_name]:
            print("Getting from cache")
            return storage[func_name][args]
        
        result = func(*args)
        
        if func_name not in storage:
            storage[func_name] = {}
        storage[func_name][args] = result
        
        print("Calculating new result")
        return result
    
    return wrapper

