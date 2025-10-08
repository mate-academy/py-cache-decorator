from typing import Callable, Any

# Główny, globalny cache, przechowujący cache dla każdej funkcji
GLOBAL_CACHE = {}


def cache(func: Callable) -> Callable:
    # 1. Inicjalizacja: Daj każdej funkcji jej własny słownik cache'u
    GLOBAL_CACHE[func] = {}

    def wrapper(*args, **kwargs) -> Any:

        # 2. Tworzenie klucza: Łączymy args i kwargs w niemutowalną krotkę
        cache_key = (args, tuple(sorted(kwargs.items())))

        # 3. Sprawdzenie Cache'u
        if cache_key in GLOBAL_CACHE[func]:
            print("Getting from cache")
            return GLOBAL_CACHE[func][cache_key]

        # 4. Obliczanie i Zapis
        else:
            print("Calculating new result")
            # Wywołujemy faktyczne, długie obliczenia
            result = func(*args, **kwargs)

            # Zapisujemy wynik przed zwróceniem
            GLOBAL_CACHE[func][cache_key] = result
            return result

    return wrapper
