class MyClass:
    # Constructor with default parameter
    def __init__(self, initial_value=0):
        self.value = initial_value

    def __del__(self):
        print("Destructor for Class")


# Creating objects using the constructor
obj1 = MyClass()  # Uses the default value (0)
obj2 = MyClass(10)  # Uses the provided value (10)

# Accessing the value attribute
print(obj1.value)  # Output: 0
print(obj2.value)  # Output: 10
