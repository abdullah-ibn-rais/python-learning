*String Things*
**different quotation no difference '..' / ".."**
**Multiline string """/''' .... """/'''**
**Quotation** --> need to use opposite kind of quotes '"Hi",said she.' , vice versa ( or use /" or /' )
**str_plus_str = my_str_1 + ' ' + my_str_2**
Concatenation possible
**Different types can not be concatenated , can use str()**
```python
name = 'John Doe'
age = 26

print(name + age) # TypeError: can only concatenate str (not "int") to str

print(name + str(age)) # John Doe26
```
**same shit :**
```python
name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string
```
**embed variables or expressions inside replacement fields**
```python
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old
```
**len(string) # 6**
```python
my_str = 'Hello world'
print(my_str[-1])  # d
```
**string[start:stop] # stop index is non-inclusive ( upto)**
start blank -> 0
stop blank -> from start to end
```python
print(my_str[:])  # Hello world
```
**string[start:stop:step] ( optional)**
```python
my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd
print(my_str[::-1]) # dlrow olleH
```
**check if exist in a string**
```python
print('hey' in my_str)    # False
```
**str**
`.upper()` -> uppercase (str.isupper()-> true)
`.lower()` -> lowercase (str.islower()-> true)
`.strip()` -> front and end space
`.replace(old,new)` -> replace all
`.split()` -> split by separator ( default space )
 `'iterable'.join(str)` -> joined_str
`.startswith(prefix)` # boolean
`.endswith(suffix)` # boolean
`.find(substring)` -> first occurance index ( default -1)
`.count(substring)` -> how many times occured
`.capitalize()` hihi
`.title()` -> first letter of each word capitalized
---

## Integers & Floats
`int` - whole numbers
`float` - decimal numbers
```python
my_int_1 = 56
my_int_2 = -4
my_float_1 = -12.0
my_float_2 = 4.9
```
## Operations
```python
# Arithmetic
sum_ints = my_int_1 + my_int_2
diff_ints = my_int_1 - my_int_2
product_ints = my_int_1 * my_int_2
div_ints = my_int_1 / my_int_2

# Mixed types → float
sum_int_and_float = my_int + my_float  # 61.4 (float)
```
## Advanced Operations
```python
# Modulo (%)
mod_ints = my_int_1 % my_int_2  # 8

# Floor Division (//)
floor_div_ints = my_int_1 // my_int_2  # 4

# Exponentiation (**)
exp_ints = my_int_1 ** my_int_2

# pow()
pow(2, 3)    # 8
pow(2, 3, 5) # 3
```
## Type Conversion
```python
float(my_int_1)     # 56.0
int(my_float)       # 12 (truncates)
int('45')           # 45
float('7.8')        # 7.8
```
## Methods
```python
round(4.798)        # 5
round(4.253, 1)     # 4.3
abs(-15)            # 15
bin(56)             # '0b111000'
oct(56)             # '0o70'
hex(56)             # '0x38'
```
# Augmented Assignment
## Concept
`variable <operator>= value` ≡ `variable = variable <operator> value`
## Examples
```python
# Addition
my_var = 10
my_var += 5  # 15

# Subtraction
count = 14
count -= 3   # 11

# Multiplication
product = 65
product *= 7 # 455

# Division
price = 100
price /= 4   # 25.0

# Floor Division
total_pages = 23
total_pages //= 5  # 4

# Modulus
bits = 35
bits %= 2    # 1

# Exponentiation
power = 2
power **= 3  # 8
```
## With Strings
```python
# Concatenation
greet = 'Hello'
greet += ' World'  # 'Hello World'

# Repetition
greet = 'Hello'
greet *= 3         # 'HelloHelloHello'

# Errors with strings
greet -= 'World'   # TypeError
greet /= 'World'   # TypeError
```
## Note
**No ****`++`**** or ****`--`**** in Python**
`++x` just does `+(+x)` → no increment
Use `x += 1` instead

# Function
## Built-in Examples
```python
name = input('What is your name?')  # User input
print('Hello', name)

int(3.14)    # 3
int('42')    # 42
int(True)    # 1
int(False)   # 0
```
## Custom Functions
```python
def calculate_sum(a, b):
    print(a + b)

calculate_sum(3, 1)  # 4
calculate_sum()  # TypeError: missing 2 required args

**# Returns value**
def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(3, 1)
print(my_sum)  # 4
```
## Key Points
* `def` keyword
* Indentation defines code blocks (4 spaces recommended)
* Parameters = placeholder variables
* Arguments = values passed when calling
* `return` exits function with value (default: `None`)

# Scope
## LEGB Rule
**L**ocal → function/class
**E**nclosing → nested functions
**G**lobal → top level/module
**B**uilt-in → Python predefined
## Local Scope
```python
def my_func():
    my_var = 10  # Local to my_func
    print(my_var)

my_func()  # 10
print(my_var)  # NameError
```
## Enclosing Scope
```python
def outer_func():
    msg = 'Hello there!'
    
    def inner_func():
        print(msg)  # Can access outer's variable
    
    inner_func()

outer_func()  # Hello there!

# Outer cannot access inner's variables
def outer_func():
    msg = 'Hello there!'
    print(res)  # NameError
    
    def inner_func():
        res = 'How are you?'
    
    inner_func()
```
## Using `nonlocal`
```python
def outer_func():
    msg = 'Hello there!'
    res = ""
    
    def inner_func():
        nonlocal res  # Modify enclosing variable
        res = 'How are you?'
        print(msg)
    
    inner_func()
    print(res)

outer_func()  
# Hello there!
# How are you?
```
## Global Scope
```python
my_var = 100  # Global

def show_var():
    print(my_var)  # Can access global

show_var()  # 100
print(my_var)  # 100
```
## Using `global`
```python
# Create global from inside function
def show_vars():
    global my_var_2
    my_var_2 = 10

show_vars()
print(my_var_2)  # 10

# Modify global variable
my_var = 10

def change_var():
    global my_var
    my_var = 20

change_var()
print(my_var)  # 20
```
## Built-in Scope
```python
print(str(45))  # '45'
print(type(3.14))  # <class 'float'>
print(isinstance(3, str))  # False
```

# Conditional Statements
## Comparison Operators
|Operator|Name|Returns True When|
|---|---|---|
|`==`|Equal|Values are equal|
|`!=`|Not equal|Values are different|
|`>`|Greater than|Left > Right|
|`<`|Less than|Left < Right|
|`>=`|Greater or equal|Left ≥ Right|
|`<=`|Less or equal|Left ≤ Right|
```python
print(3 > 4)   # False
print(3 < 4)   # True
print(3 == 4)  # False
print(4 == 4)  # True
print(3 != 4)  # True
print(3 >= 4)  # False
print(3 <= 4)  # True
```
## `if` Statement
```python
if condition:
    # Code if True

age = 18
if age >= 18:
    print('You are an adult')  # Runs
```
## `if-else`
```python
age = 12
if age >= 18:
    print('You are an adult')
else:
    print('You are not an adult yet')  # Runs
```
## `if-elif-else`
```python
age = 12
if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child')  # Runs
```
## Multiple `elif`
```python
age = 2
if age >= 65:
    print('You are a senior citizen')
elif age >= 30:
    print('You are an adult in your prime')
elif age >= 18:
    print('You are a young adult')
elif age >= 13:
    print('You are a teenager')
elif age >= 3:
    print('You are a young child')
else:
    print('You are a toddler or an infant')  # Runs
```

# Truthy/Falsy Values
## Falsy Values (Complete List)
```python
None
False
0 (int)
0.0 (float)
0j (complex zero)
"" (empty string)
[] (empty list)
{} (empty dict)
() (empty tuple)
set() (empty set)
range(0) (empty range)
bytes(0) (empty bytes)
bytearray(0) (empty bytearray)
memoryview(b'') (empty memoryview)
```
## Truthy Values (Examples)
```python
True
1, -1, 100 (non-zero numbers)
3.14 (non-zero float)
(1+2j) (non-zero complex)
"hello" (non-empty string)
[1,2,3] (non-empty list)
{"a": 1} (non-empty dict)
(1,2) (non-empty tuple)
{1,2} (non-empty set)
range(5) (non-empty range)
b"hello" (non-empty bytes)
```
## `bool()` Check
```python
bool(False)   # False
bool(0)       # False
bool("")      # False
bool([])      # False
bool({})      # False
bool(())      # False
bool(set())   # False

bool(True)    # True
bool(1)       # True
bool("Hello") # True
bool([1])     # True
bool({"a":1}) # True
```
## Logical Operators
### `and`
```python
# Returns first falsy or last truthy
print(True and 25)  # 25
print(False and 25) # False
print(0 and 25)     # 0

# Short-circuits on first falsy
if is_citizen and age >= 18:
    print('Eligible to vote')
```
### `or`
```python
# Returns first truthy or last falsy
print(19 or False)  # 19
print(0 or False)   # False
print("" or "backup")  # "backup"

# Short-circuits on first truthy
if age < 18 or is_student:
    print('Student discount')
```
### `not`
```python
not ""        # True (falsy → True)
not "Hello"   # False (truthy → False)
not 0         # True
not 1         # False
not False     # True
not True      # False

# Usage
if not is_admin:
    print('Access denied')
```
## Examples
```python
# Nested condition
is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('Eligible to vote')  # Runs
else:
    print('Not eligible')

# Using and
if is_citizen and age >= 18:
    print('Eligible to vote')  # Runs

# Using or
if age < 18 or is_student:
    print('Student discount')
```

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

```python
list_c = [4, 5, 6]
list_d = list_c  # list_d now points to the exact same object as list_c

# Check if they are the exact same object
print(list_c is list_d)
# Output: True (They share the same memory address)

list_a = [1, 2, 3]
list_b = [1, 2, 3]

# Check if they are the exact same object
print(list_a is list_b)
# Output: False (They are two separate objects in memory)

list_a = [1, 2, 3]
list_b = [1, 2, 3]

# Check if the values are the same
print(list_a == list_b)
# Output: True (The content is the same)


```

```python


```




```python

```


```python

```


```python

```

