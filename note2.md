import re


medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]


def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):

    constraints = {
        'patient_id': isinstance(patient_id, str)
        and re.fullmatch('p\d+', patient_id, re.IGNORECASE),
        'age': isinstance(age, int) and age >= 18,
        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,
        'medications': isinstance(medications, list)
        and all([isinstance(i, str) for i in medications]),
        'last_visit_id': isinstance(last_visit_id, str)
        and re.fullmatch('v\d+', last_visit_id, re.IGNORECASE)
    }

    return [key for key, value in constraints.items() if not value]


def validate(data):
    is_sequence = isinstance(data, (list, tuple))

    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False
        
    is_invalid = False
    key_set = set(
        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
    )

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue

        if set(dictionary.keys()) != key_set:
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True
            continue

        invalid_records = find_invalid_records(**dictionary)
        for key in invalid_records:
            print(f"Unexpected format '{key}: {dictionary[key]}' at position {index}.")
            is_invalid = True
    if is_invalid:
        return False
    print('Valid format.')
    return True

validate(medical_records)


# Classes & Objects

## Class Definition
```python
class Dog:
    species = "French Bulldog"  # Class attribute
    
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age
    
    def bark(self):
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")
```

## Creating Objects
```python
dog_1 = Dog("Jack", 3)
dog_2 = Dog("Thatcher", 5)

dog_1.bark()  # JACK says woof woof! I'm 3 years old!
dog_2.bark()  # THATCHER says woof woof! I'm 5 years old!
```

## Class vs Instance Attributes
```python
print(Dog.species)     # French Bulldog (class attribute)
print(dog_1.name)      # Jack (instance attribute)
print(dog_1.species)   # French Bulldog (shared class attribute)
```

## Car Example
```python
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    
    def describe(self):
        return f"This car is a {self.color} {self.model}"

car_1 = Car("red", "Toyota Corolla")
print(car_1.describe())  # This car is a red Toyota Corolla
```

---

# Special Methods (Dunder Methods)

## Without Special Methods
```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

print(len(book1))      # TypeError
print(str(book1))      # <__main__.Book object at 0x...>
print(book1 == book2)  # False (compares memory addresses)
```

## With Special Methods
```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __len__(self):
        return self.pages
    
    def __str__(self):
        return f"'{self.title}' has {self.pages} pages"
    
    def __eq__(self, other):
        return self.pages == other.pages

print(len(book1))      # 420
print(str(book1))      # 'Built Wealth Like a Boss' has 420 pages
print(book1 == book2)  # True
```

## Shopping Cart Example
```python
class Cart:
    def __init__(self):
        self.items = []
    
    def add(self, item):
        self.items.append(item)
    
    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} is not in cart')
    
    def list_items(self):
        return self.items
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __contains__(self, item):
        return item in self.items
    
    def __iter__(self):
        return iter(self.items)

cart = Cart()
cart.add('Laptop')
cart.add('Wireless mouse')

print(len(cart))           # 2
print('Laptop' in cart)    # True
for item in cart:          # Laptop Wireless mouse
    print(item)
```

---

# Dynamic Attribute Handling

## `getattr()`
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('John Doe', 30)
print(getattr(person, 'name'))        # John Doe
print(getattr(person, 'city', 'Milano'))  # Milano (default)

# Dynamic from variable
attr_name = input('Enter attribute: ')
print(getattr(person, attr_name, 'Attribute not found'))
```

## `dir()` to List Attributes
```python
for attr in dir(person):
    if not attr.startswith('__') and not callable(getattr(person, attr)):
        value = getattr(person, attr)
        print(f'{attr}: {value}')
# age: 30
# name: John Doe
```

## `setattr()`
```python
class Configuration:
    pass

settings_data = {
    'server_url': 'https://api.example.com',
    'timeout_sec': 30,
    'max_retries': 5
}

config_obj = Configuration()
for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)

print(config_obj.server_url)  # https://api.example.com
```

## `hasattr()`
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product_a = Product('T-Shirt', 25)
required_attributes = ['name', 'price', 'inventory_id']

for attr in required_attributes:
    if not hasattr(product_a, attr):
        print(f"ERROR: Missing attribute: '{attr}'")
    else:
        print(f'{attr}: {getattr(product_a, attr)}')
```

## `delattr()`
```python
class UserSession:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.auth_token = token  # sensitive
        self.temp_counter = 0    # temporary

session = UserSession(101, 'a1b2c3d4e5')
attributes_to_clean = ['auth_token', 'temp_counter']

for attr in attributes_to_clean:
    if hasattr(session, attr):
        delattr(session, attr)
        print(f'Removed attribute: {attr}')
```