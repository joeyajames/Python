class Base:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Child(Base):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def get_age(self):
        return self.age


Child.func2 = lambda num: num ** 2
obj = Child("suneesh", 40)
obj.func = lambda num: num * 2
print(obj.get_name(), obj.get_age())

print(obj.func(2))
print(Child.func2(5))

print(obj.__dict__)
print(Child.__dict__)
print(Base.__dict__)

print(obj.name)
print(obj.__dict__['name'])
