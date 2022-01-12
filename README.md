# Cache decorator
- Read the [guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md)  before start

У тебя есть большой массив данных. Тебе нужно пропустить эти данные через
функцию с большим временем выполнения. Данные в массиве могут повторяться.
Чтобы повторно не вызывать функцию для повторяющихся данных, было бы
отлично сохранять значение результата выполнения функции с этими данными.

Напиши декоратор `cache` который сохраняет результаты выполнения функции 
с разными аргументами и если функция вызывается с аргументами, с которыми она уже вызывалась - 
`cache` должен возвращать сохраненное значение, а не вызывать функцию 
заново. Декоратором `cache` можно декорировать только те функции, 
которые принимают только **неизменяемые** объекты.

Так же учти, что декоратор `cache` должен правильно работать с 
несколькими задекорированными функциями одновременно и верно возвращать
значение для каждой функции отдельно.

Так же `cache` должен выводить `Getting from cache` когда возвращает 
существующий результат и `Calculating new result` когда запускает 
функцию.

Пример:
```python
@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a*c)

@cache
def long_time_func_2(a, b, c):
    return a * b * c / (a + b)

long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2(1, 2, 3)
long_time_func(1, 2, 3)
long_time_func_2(3, 2, 3)
long_time_func_2(3, 2, 3)

# Calculating new result 
# Calculating new result 
# Calculating new result 
# Getting from cache 
# Calculating new result 
# Getting from cache
```
