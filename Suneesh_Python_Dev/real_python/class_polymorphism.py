class Parent:
    def __init__(self):
        self.name = "Parent Class"

    def display(self):
        print("PARENT : Nothing to display")


class Child(Parent):
    def __init__(self):
        self.name = "Child Class"

    def display(self):
        print("CHILD : Nothing to display")


def func(obj):
    obj.display()


def test_overloading_static_polymorphism():
    print("Static Polymorphism...")
    child_obj = Child()
    parent = Parent()
    func(child_obj)
    func(parent)


class Animal():
    def __init__(self, age):
        self.name = "Animal" + str(age)

    def speak(self):
        raise NotImplementedError("Subclass must implement this method")


class Dog(Animal):

    def __init__(self, age):
        self.name = "Dog" + str(age)

    def speak(self):
        return "Woof!"


class Cat(Animal):
    def __init__(self, age):
        self.name = "Cat" + str(age)

    def speak(self):
        return "Meow!"


def test_overriding_dynamic_polymorphism():
    print("Dynamic Polymorphism...")
    # Create a list of Animal objects
    animals = [Dog(3), Cat(5)]
    # Call the speak method on each object
    for animal in animals:
        print(animal.speak())
        print(animal.name)


test_overriding_dynamic_polymorphism()

# test_overloading_static_polymorphism()
