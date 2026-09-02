from typing import Callable


def cache(func: Callable) -> Callable:
    storage = []
    def wrapper(*args):
        func_name = func.__name__
        # 1. Verificar se já existe dicionário com nome da função
        for item in storage:
            if func_name in item:
                # 2. Verificar se argumentos já existem
                if args in item[func_name]:
                    return "Getting from cache"
                else:
                    # 3. Adicionar novos argumentos ao dicionário existente
                    storage.append(item[func_name][args])
                    return "Calculating new result"
            else:
                # 4. Se não encontrou, criar novo dicionário na lista
                storage.append(item[func_name][args])
                return "Calculating new result"
    return wrapper
