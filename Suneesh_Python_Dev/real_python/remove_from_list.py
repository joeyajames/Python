a = [x for x in range(1, 11)]
a.extend([4, 5, 6, 7, 5, 5, 5, 5])
print(a)

b = a.remove(5)
print(a)
print(b)

c = a.pop(2)
print(a)
print(c)
