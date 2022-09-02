# Cache decorator
- Read the [guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md)  before start

You have a big array with data. You have to run a long runtime function
with this data. Data can be repeated.
To not re-run function with repeatable data, it will be good to store
results of completed runs.

Write decorator `cache` that stores results of completed runs with
different arguments, number of arguments can be also different.
If decorated function runs with repeating arguments it should return stored
result instead of calling function again. Decorator `cache` creating for 
decorating only functions that take **immutable** arguments.

Also note, that decorator `cache` should work correctly with few decorated
functions simultaneously and correctly return for every function separately.

Also `cache` should print `Getting from cache` when returns stored value and 
`Calculating new result` when run function with new arguments.

Example:
```python
@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple, power):
    return [number ** power for number in n_tuple]

long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)

# Calculating new result 
# Calculating new result 
# Calculating new result 
# Getting from cache 
# Calculating new result 
# Getting from cache
```

# Сhecklist (read before push)

Сheck your code against the following points

1. **CODE EFFICIENCY:** don't call the same function several times, store result and use it.

Bad example:
```python
animals = "cat, dog, rabbit"
print(animals.title())

for letter in set(animals.title()):
    if animals.title().count(letter) > 1:
        print("wow")
```
Good example:
```python
animals = "cat, dog, rabbit"
animals_title = animals.title()
print(animals_title)

for letter in set(animals_title):
    if animals_title.count(letter) > 1:
        print("wow")
```
2. **DON`T REPEAT YOURSELF:** write your code so that you don't 
   have duplicated lines or whole blocks of code.

Bad example:
```python
if "cat" in animal_list:
    print("found")
    print("the end")
else:
    print("not found")
    print("the end")
```
Good example:
```python
if "cat" in animal_list:
    print("found")
else:
    print("not found")

print("the end")
```
3. **CODE STYLE:** use descriptive and correct variable names.

Bad example:

```python
ls = [1, 2, 3, 4]
rs = 0
for a in ls:
    rs += a
```

Good example:

```python
list_of_numbers = [1, 2, 3, 4]
result = 0
for number in list_of_numbers:
    result += number
```

4. **CODE STYLE:** use one quotes style in your code. 
Double quotes are preferable.
5. **CLEAN CODE:** you don't need `nonlocal` statement 
   when you change mutable object in inner function.
6. **CLEAN CODE:** when you write your code you can add comments, 
   prints, functions to check your solution and so on. 
   Don't forget to delete all this when you are 
   ready to commit and push your code.