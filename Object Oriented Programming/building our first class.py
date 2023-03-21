# Define the class with attributes and methods
class Student:
    def __init__(self, name, std, section=None, subjects=None):
        self.name = name
        self.std = std
        self.section = section
        self.subjects = subjects or []

# Create objects and pass values to the constructor
varun = Student("Harry", 12, section=1)
larry = Student("Larry", 9, subjects=["Hindi", "Physics"])

# Access object attributes
print(varun.section, larry.subjects)


