def display(set1):
    print(f"Type = {type(set1)}, id = {id(set1)} , value = {set1}")


dict1 = {}
dict2 = {
    "apple": 2,
    "cherry": 1,
}
dict4 = dict(
    apple=1,
    cherry=8,
)
dict3 = dict(banana=2, grapes=4)

display(dict1)
display(dict2)
display(dict3)

# Double each value in the dictionary
for ele in dict3.items():
    display(ele)

display(dict3.keys())
display(dict3.values())

list1 = [[2, 3, 4], [1, 2, 3], [0, 9, 8]]
display(list1)
list1.sort()
display(list1)

dict3.update(dict4)
display(dict3)

# Sorting Dictionary
value_reverse_dict = dict(sorted(dict3.items(), key=lambda x: x[1], reverse=True))
key_reverse_dict = dict(sorted(dict3.items(), key=lambda x: x[0], reverse=True))
display(dict3)
display(value_reverse_dict)
display(key_reverse_dict)

a, *c = dict(a=4, b=5, c=6, d=7)

display(a)
# display(b)
display(c)

print(type(iter(["1", 2])))

print(list(map(lambda a, b, c: a + b + c, [1, 2], [3, 4], [5, 6])))

t = tuple(("Suneesh",))
display(t)

n = (42,)
display(n)

dd = frozenset([1, 2, 3])
display(dd)
new_fronzen_dict = {}
new_fronzen_dict[frozenset([1, 2, 3])] = "value"
# new_fronzen_dict = dict(frozenset([1, 2, 3]), "value")
display(new_fronzen_dict)
