from dataclasses import dataclass, field
from typing import List, Optional

@dataclass(
    frozen=True,  # Make the class immutable
    order=True,   # Add ordering methods (__lt__, __le__, __eq__, __ne__, __gt__, __ge__)
    init=True,    # Include an automatically generated __init__ method
    repr=True,    # Include a __repr__ method
    eq=True,      # Include an automatically generated __eq__ method
    unsafe_hash=True,  # Disable hashing (for mutable objects)
    slots=True
)
class Person:
    name: str
    age: int
    address: str
    email: Optional[str] = None
    tags: List[str] = field(default_factory=list)

    # Custom initialization logic
    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative.")

    # Custom method
    def greet(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old."


# Example usage:

# Creating an instance with default values
person1 = Person(name="Alice", address="India", age=30)
print(person1)  # Output: Person(name='Alice', age=30, email=None, tags=[])

# Creating an instance with custom values
person2 = Person(name="Bob", address="FR", age=25, email="bob@example.com", tags=["developer", "python"])
print(person2)  # Output: Person(name='Bob', age=25, email='bob@example.com', tags=['developer', 'python'])

# Accessing attributes
print(person2.name)  # Output: 'Bob'

# Using custom method
print(person2.greet())  # Output: "Hello, my name is Bob and I'm 25 years old."

# Comparing instances (due to 'order' option)
print(person1 < person2)  # Output: False

# # Hashing instance (due to 'unsafe_hash' option)
# hash_value = hash(person1)
# print(hash_value)


print(Person.__dict__)
# print(Person.__slots__) # enabled when slots are enabled in dataclass

# print(person1.__slots__)
# print(person1.__dict__)

