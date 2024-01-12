from collections import namedtuple
from copy import deepcopy


def display_tuple(tuple_to_display):
    print(f"type = {type(tuple_to_display)}, id = {id(tuple_to_display)} , value = {tuple_to_display}")


name = ("Suneesh", "Mohan", "Joshi")
address = ("52", "maidnehad", "uk")

display_tuple(name)
display_tuple(address)

*head, tail = name
display_tuple(head)
display_tuple(tail)

combined = (*name, *address)
display_tuple(combined)
combined2 = name + address

display_tuple(combined2)

print("-" * 20)
name2 = name
display_tuple(name)
display_tuple(name2)
name3 = name[:]
display_tuple(name3)

name4 = deepcopy(name)
display_tuple(name4)

name += ("More", "Text")
display_tuple(name)

numbers = (42,)
display_tuple(numbers)

Person = namedtuple("Person", "first middle last")
a = Person(*name2)
display_tuple(a)

list_name = list(name2)
display_tuple(list_name)
# del name2[1]  #  Not Allowed in tuple
del list_name[1]  # Allowed in list
display_tuple(list_name)

new_tuple = ("Aadya", "Suneesh", ["Joshi"])
display_tuple(new_tuple)

new_tuple[2].insert(0, "Test")
new_tuple[2].pop()

display_tuple(new_tuple)

new_tuple[2] = ["New List"]
