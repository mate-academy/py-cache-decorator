from functools import wraps

def cache(func):
    storage = {}

    @wraps(func)
    def wrapper(*args):  # тільки позиційні аргументи
        key = args  # ключ кешу будуємо тільки з args
        if key in storage:
            print("Getting from cache")
            return storage[key]
        print("Calculating new result")
        result = func(*args)
        storage[key] = result
        return result

    return wrapper