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

