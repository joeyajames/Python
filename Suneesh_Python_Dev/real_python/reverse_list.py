a = [1, 2, 3, 4, 5, 6]
b = reversed(a)
print(a)
print(b)
for i in b:
    print(i)

print(id(a))
print(id(b))

print(a)
a.reverse()
print(a)

big_list = list(range(0, 10))
print(big_list)
print(big_list[len(big_list) - 1::-1])
print(big_list[slice(None, None, -1)])

print([big_list[index] for index in range(len(big_list) - 1, -1, -1)])


# Testing default value in function arguments
def append_to(item, target=[]):
    target.append(item)
    return target


print(append_to(1))
print(append_to(2))
print(append_to(3))
