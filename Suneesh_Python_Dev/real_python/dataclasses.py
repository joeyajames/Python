from dataclasses import dataclass


@dataclass
class Person:
    name: str


person = Person(name="Suneesh")
print(person)
