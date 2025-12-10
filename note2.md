# Lists

## Basics

```python
cities = ['Los Angeles', 'London', 'Tokyo']
cities[0]    # 'Los Angeles'
cities[-1]   # 'Tokyo'
len(numbers) # 5

```

## Creation

```python
list('Jessica')  # ['J','e','s','s','i','c','a']

```

## Update/Delete

```python
programming_languages[0] = 'JavaScript'  # Modify
del developer[1]  # Remove element
'Rust' in programming_languages  # True

```

## Nested Lists

```python
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2]        # ['Python', 'Rust', 'C++']
developer[2][1]     # 'Rust'

```

## Unpacking

```python
name, age, job = ['Alice', 34, 'Rust Dev']
# name='Alice', age=34, job='Rust Dev'

name, *rest = ['Alice', 34, 'Rust Dev']
# name='Alice', rest=[34, 'Rust Dev']

```

## Slicing

```python
desserts[1:4]    # ['Cookies', 'Ice Cream', 'Pie']
numbers[1::2]    # [2, 4, 6]  (even indices)

```

## Methods

### Add Elements

```python
numbers.append(6)        # [1,2,3,4,5,6]
numbers.append([6,8,10]) # [1,2,3,4,5,[6,8,10]]
numbers.extend([6,8,10]) # [1,2,3,4,5,6,8,10]
numbers.insert(2, 2.5)   # [1,2,2.5,3,4,5]

```

### Remove Elements

```python
numbers.remove(5)        # Removes first 5
numbers.pop(1)           # Removes element at index 1
numbers.pop()            # Removes last element
numbers.clear()          # []

```

### Sort/Reverse

```python
numbers.sort()           # Sorts in-place
sorted(numbers)          # Returns new sorted list
numbers.reverse()        # Reverses in-place

```

### Search

```python
programming_languages.index('Java')  # 1
# ValueError if not found

```

## Notes

- Mutable, zero-based indexing
- `IndexError` if index out of bounds
- `ValueError` if unpack mismatch or element not found

# Tuples

## Basics

```python
developer = ('Alice', 34, 'Rust Developer')
developer[1]    # 34
developer[-2]   # 34
len(developer)  # 3
tuple('Jessica') # ('J','e','s','s','i','c','a')

```

## Immutable

```python
programming_languages[0] = 'JavaScript'  # TypeError
del developer[1]  # TypeError

```

## Operations

```python
'Rust' in programming_languages  # True

```

## Unpacking

```python
name, age, job = ('Alice', 34, 'Rust Dev')
name, *rest = ('Alice', 34, 'Rust Dev')
# rest = [34, 'Rust Dev']

```

## Slicing

```python
desserts = ('cake', 'pie', 'cookies', 'ice cream')
desserts[1:3]  # ('pie', 'cookies')

```

## Methods

### `count()`

```python
programming_languages.count('Rust')  # 2
programming_languages.count('JavaScript')  # 0
**programming_languages.count()  # TypeError**

```

### `index()`

```python
programming_languages.index('Java')  # 1
**programming_languages.index('JavaScript')  # ValueError**
programming_languages.index('Python', 3)  # 5 (start at index 3)
programming_languages.index('Python', 2, 5)  # 2 (start=2, stop=5)

```

## Sorting

```python
sorted(numbers)  # Returns new sorted list
sorted(programming_languages, key=len)  # Sort by length
sorted(programming_languages, reverse=True)  # Reverse sort

```

## Notes

- Immutable (vs lists which are mutable)
- Use for fixed, unchanging data
- `tuple()` constructor works with any iterable
- `sorted()` returns new list, doesn't modify tuple

# Loops

## `for` Loop

```python
for language in ['Rust', 'Java', 'Python', 'C++']:
    print(language)
# Rust
# Java
# Python
# C++

for char in 'code':
    print(char)
# c
# o
# d
# e

```

## Nested `for` Loops

```python
for category in ['Fruit', 'Vegetable']:
    for food in ['Apple', 'Carrot', 'Banana']:
        print(category, food)
# Fruit Apple
# Fruit Carrot
# Fruit Banana
# Vegetable Apple
# Vegetable Carrot
# Vegetable Banana

```

## `while` Loop

```python
secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess (1-5): '))
    if guess != secret_number:
        print('Wrong! Try again.')

print('You got it!')

```

## `break` Statement

```python
for developer in ['Jess', 'Naomi', 'Tom']:
    if developer == 'Naomi':
        break
    print(developer)  # Only 'Jess'

```

## `continue` Statement

```python
for developer in ['Jess', 'Naomi', 'Tom']:
    if developer == 'Naomi':
        continue
    print(developer)  # 'Jess', 'Tom'

```

## `else` Clause with Loops

```python
for word in ['sky', 'apple', 'rhythm', 'fly', 'orange']:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")
# 'sky' has no vowels
# 'apple' contains vowel 'a'
# 'rhythm' has no vowels
# 'fly' has no vowels
# 'orange' contains vowel 'o'
**# else executes if the whole loop successfully finish**
```

## Notes

- Indentation required for loop body
- `break` exits loop immediately
- `continue` skips to next iteration
- `else` runs only if loop completes without `break`
- `while` runs until condition is `False`

# Ranges

## Syntax

```python
range(stop)           # 0 to stop-1
range(start, stop)    # start to stop-1
range(start, stop, step)

```

## Examples

```python
for num in range(3):
    print(num)        # 0, 1, 2

for num in range(1, 5):
    print(num)        # 1, 2, 3, 4

for num in range(2, 11, 2):
    print(num)        # 2, 4, 6, 8, 10

for num in range(40, 0, -10):
    print(num)        # 40, 30, 20, 10

```

## Notes

```python
list(range(2, 11, 2))  # [2, 4, 6, 8, 10]
range()                # TypeError (needs 1 arg)
range(1.5, 5)          # TypeError (no floats)

```

---

# `enumerate()`

```python
list(enumerate(['Spanish', 'English']))
# [(0, 'Spanish'), (1, 'English')]

for index, language in enumerate(['Spanish', 'English']):
    print(f'Index {index}: {language}')

for index, language in enumerate(['Spanish', 'English'], 1):
    print(f'Index {index}: {language}')
# Index 1: Spanish
# Index 2: English

```

---

# `zip()`

```python
list(zip(['Naomi', 'Dario'], [1, 2]))
# [('Naomi', 1), ('Dario', 2)]

for name, id in zip(['Naomi', 'Dario'], [1, 2]):
    print(f'Name: {name}, ID: {id}')
    
# Name: Naomi, ID: 1
# Name: Dario, ID: 2
```

---

```python
names = ['Alice', 'Bob', 'Charlie', 'Dana']

custom_ids = range(10, 10 + len(names))
# custom_ids is: (10, 11, 12, 13)

# enumerate(names) generates: (0, 'Alice'), (1, 'Bob'), (2, 'Charlie'), (3, 'Dana')
for id_val, (index, name) in zip(custom_ids, enumerate(names)):
    print(f"ID: {id_val} | Index: {index} | Name: {name}")

# ID: 10 | Index: 0 | Name: Alice
# ID: 11 | Index: 1 | Name: Bob
# ID: 12 | Index: 2 | Name: Charlie
# ID: 13 | Index: 3 | Name: Dana
```

# List Comprehensions

```python
even_numbers = [num for num in range(21) if num % 2 == 0]

numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
# [(1,'Odd'), (2,'Even'), (3,'Odd'), (4,'Even'), (5,'Odd')]
```

---

# Useful Functions

## `filter()`

```python
def is_long_word(word):
    return len(word) > 4

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']
long_words = list(filter(is_long_word, words))
# ['mountain', 'river', 'cloud']
```

## `map()`

```python
def to_fahrenheit(temp):
    return (temp * 9/5) + 32

celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(to_fahrenheit, celsius))
# [32.0, 50.0, 68.0, 86.0, 104.0]
```

## `sum()`

```python
sum([5, 10, 15, 20])          # 50
sum([5, 10, 15, 20], 10)      # 60
sum([5, 10, 15, 20], start=10) # 60
```

---

# Lambda Functions

```python
lambda num: num ** 2

# With filter()
even_numbers = list(filter(lambda x: x % 2 == 0, [1,2,3,4,5]))
# [2, 4]

# ❌ Don't assign to variable
square = lambda x: x ** 2  # Bad

# ✅ Use regular function instead
def square(num):
    return num ** 2

# ❌ Avoid complex lambdas
result = (lambda x: (x**2 + 2*x - 1) if x > 0 else (x**3 - x + 4))(3)
# Hard to read

# ✅ Better with regular function
def calculate_expression(x):
    if x > 0:
        return x**2 + 2*x - 1
    else:
        return x**3 - x + 4

```